from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from .models import BragDocument
from .utils import extract_employee_data, generate_brag_document
import os
import json

@login_required(login_url='/auth/signin/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/auth/signin/')
def history(request):
    documents = BragDocument.objects.filter(user=request.user)
    return render(request, 'history.html', {'documents': documents})

@csrf_exempt
def generate(request):
    if request.method == 'POST':
        file_path = None
        try:
            employee_name = request.POST.get('employee_name')
            month = request.POST.get('month')
            excel_file = request.FILES.get('excel_file')
            
            if not all([employee_name, month, excel_file]):
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            print("default storage: ", default_storage)
            file_path = default_storage.save(f'temp/{excel_file.name}', excel_file)
            full_path = default_storage.path(file_path)
            
            employee_data = extract_employee_data(full_path, employee_name, month)
            
            if not employee_data:
                return JsonResponse({'error': 'No data found for the specified employee and month'}, status=404)
            
            result = generate_brag_document(employee_data)
            
            brag_doc = BragDocument.objects.create(
                user=request.user,
                employee_name=employee_name,
                month=month,
                work_accomplishments=result.work_accomplishments.dict(),
                learning=result.learning,
                utilized_skills=result.utilized_skills
            )
            
            return JsonResponse({
                'id': brag_doc.id,
                'employee_name': employee_name,
                'month': month,
                'work_accomplishments': result.work_accomplishments.dict(),
                'learning': result.learning,
                'utilized_skills': result.utilized_skills
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        finally:
            if file_path and default_storage.exists(file_path):
                default_storage.delete(file_path)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@login_required(login_url='/auth/signin/')
def view_document(request, doc_id):
    try:
        doc = BragDocument.objects.get(id=doc_id, user=request.user)
        return render(request, 'view_document.html', {'document': doc})
    except BragDocument.DoesNotExist:
        return HttpResponse('Document not found', status=404)

@login_required(login_url='/auth/signin/')
def export_markdown(request, doc_id):
    try:
        doc = BragDocument.objects.get(id=doc_id, user=request.user)
        
        markdown = f"# Brag Document - {doc.employee_name} ({doc.month})\n\n"
        markdown += "## WORK ACCOMPLISHMENTS\n\n"
        
        wa = doc.work_accomplishments
        markdown += "### Goals of this Quarter:\n"
        for item in wa['goals_of_this_quarter']:
            markdown += f"- {item}\n"
        
        markdown += "\n### Goals of this Month:\n"
        for item in wa['goals_of_this_month']:
            markdown += f"- {item}\n"
        
        markdown += "\n### Official Project Accomplishments:\n"
        for item in wa['official_project_accomplishments']:
            markdown += f"- {item}\n"
        
        markdown += "\n### Personal Project Accomplishments:\n"
        for item in wa['personal_project_accomplishments']:
            markdown += f"- {item}\n"
        
        markdown += "\n### Personal Reflection:\n"
        pr = wa['personal_reflection']
        markdown += "#### What I am Most Proud Of:\n"
        for item in pr['what_i_am_most_proud_of']:
            markdown += f"- {item}\n"
        
        markdown += "\n#### Areas I am Focused On For Growth:\n"
        for item in pr['areas_i_am_focused_on_for_growth']:
            markdown += f"- {item}\n"
        
        markdown += "\n## LEARNING\n\n"
        for item in doc.learning:
            markdown += f"- {item}\n"
        
        markdown += "\n## UTILIZED SKILLS\n\n"
        for item in doc.utilized_skills:
            markdown += f"- {item}\n"
        
        response = HttpResponse(markdown, content_type='text/markdown')
        response['Content-Disposition'] = f'attachment; filename="brag_document_{doc.employee_name}_{doc.month}.md"'
        return response
        
    except BragDocument.DoesNotExist:
        return HttpResponse('Document not found', status=404)
