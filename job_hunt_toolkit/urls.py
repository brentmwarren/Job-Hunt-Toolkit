from django.urls import path
from . import views

urlpatterns = [
    path('', views.application_list, name='application_list'),
    path('applications/new/', views.application_create, name='application_create'),
    path('applications/<int:pk>', views.application_detail, name='application_detail'),
    path('applications/<int:pk>/edit', views.application_edit, name='application_edit'),
    path('applications/<int:pk>/delete', views.application_delete, name='application_delete'),
]