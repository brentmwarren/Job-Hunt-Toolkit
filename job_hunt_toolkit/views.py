
from django.shortcuts import render
from .models import Application
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_http_methods


# from .models import Checklist
# from .forms import ChecklistForm
from .models import Application
from .forms import ApplicationForm


# Create your views here.

def home(request):
    return HttpResponse("Goodbye rocket ship. Hello Home.")

def application_list(request):
    applications = Application.objects.all()
    return render(request, 'application_list.html', {'applications': applications})

@login_required
def application_create(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # application["user"] = "put in user id from django admin portal"
            application = form.save()
            return redirect('application_list', pk=application.pk)
    else:
        form = ApplicationForm()
    return render(request, 'application_form.html', {'form': form}) 

def application_detail(request, pk):
    application = Application.objects.get(id=pk)
    return render(request, 'application_detail.html', {'application': application})       

def application_edit(request, pk):
    application = Application.objects.get(pk=pk)
    if request.method == "POST":
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            artist = form.save()
            return redirect('application_list', pk=application.pk)
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'application_form.html', {'form': form})   

def application_delete(request, pk):
    Application.objects.get(id=pk).delete()
    return redirect('application_list')     

# def checklist_list(request):
#     checklist = Checklist.objects.all()
#     return render(request, 'checklist_list.html', {'checklist': checklist})