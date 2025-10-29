from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('generate/', views.generate, name='generate'),
    path('get-models/', views.get_models, name='get_models'),
    path('history/', views.history, name='history'),
    path('document/<int:doc_id>/', views.view_document, name='view_document'),

    path('export/<int:doc_id>/', views.export_markdown, name='export_markdown'),
    path('delete/<int:doc_id>/', views.delete_document, name='delete_document'),
]
