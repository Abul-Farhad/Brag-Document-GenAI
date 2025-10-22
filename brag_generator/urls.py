from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate/', views.generate, name='generate'),
    path('history/', views.history, name='history'),
    path('document/<int:doc_id>/', views.view_document, name='view_document'),
    path('export/<int:doc_id>/', views.export_markdown, name='export_markdown'),
]
