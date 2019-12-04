from django.urls import path
from . import views

urlpatterns = [
    path('', views.application_list, name='application_list'),
    path('checklist/', views.checklist_list, name='checklist_list')
]