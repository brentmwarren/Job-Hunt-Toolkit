from django.shortcuts import render
from .models import Application
from django.http import HttpResponse
# from .models import Checklist

from .forms import ApplicationForm
# from .forms import ChecklistForm

# Create your views here.

def home(request):
  return HttpResponse("Goodbye rocket ship. Hello Home.")

def application_list(request):
    applications = Application.objects.all()
    return render(request, 'application_list.html', {'applications': applications})

def application_create(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            return redirect('application_list', pk=application.pk)
    else:
        form = ApplicationForm()
    return render(request, 'application_form.html', {'form': form})

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

# def checklist_list(request):
#     checklist = Checklist.objects.all()
#     return render(request, 'checklist_list.html', {'checklist': checklist})