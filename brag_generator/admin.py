from django.contrib import admin
from .models import BragDocument

@admin.register(BragDocument)
class BragDocumentAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'month', 'generated_at']
    list_filter = ['month', 'generated_at']
    search_fields = ['employee_name', 'month']
    readonly_fields = ['generated_at']
