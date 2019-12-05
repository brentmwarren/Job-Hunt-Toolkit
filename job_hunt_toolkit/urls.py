from django.urls import path
from . import views

urlpatterns = [
    path('', views.application_list, name='application_list'),
     path('application/new/', views.application_create, name='application_create'),
    # path('checklist/', views.checklist_list, name='checklist_list')
]