from django import forms
from .models import Application
from .models import Checklist

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('name', 'job_title', 'job_url', 'date_applied', 'company_notes', 'personal_notes')

# class ChecklistForm(forms.ModelForm):

#     class Meta:
#         model = Checklist
#         fields = ('item_name','checkbox')