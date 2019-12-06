from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms.fields import DateField

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=100,)
    job_title = models.CharField(max_length=100, blank=True)
    job_url = models.CharField(max_length=100, blank=True)
    date_applied = models.DateField(null=True, blank=True)
    company_notes = models.TextField(null=True, blank=True)
    personal_notes = models.TextField(null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')

    def __str__(self):
        return self.name

class Checklist (forms.Form):
    item_name  = models.TextField(null=True, blank=True)
    checkbox = forms.BooleanField (initial = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checks')