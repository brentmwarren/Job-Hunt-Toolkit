from django.shortcuts import render
from .models import Application, Checklick

# Create your views here.

def application_list(request):
    applications = Application.objects.all()
    return render(request, 'job_hunt_toolkit/application_list.html', {'applications': applications})