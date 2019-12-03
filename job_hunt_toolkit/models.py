from django.db import models
from django.contrib.auth.models import User
from django.forms.fields import DateField

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=100,)
    job_title = models.CharField(max_length=100, blank=True)
    job_url = models.CharField(max_length=100, blank=True)
    date_applied = models.DateField(null=True, blank=True)
    company_notes = models.TextField(null=True, blank=True)
    personal_notes = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')

    def __str__(self):
        return self.name

    def hello(self):
        return f"Hello my name is.. {self.name}"

    def template(self):
        return f"<li>{self.name}</li>"

class Checklick(models.Model):
    user = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='checks')