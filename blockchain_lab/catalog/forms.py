from django import forms
from catalog.models import Procurement
from django.forms.widgets import ClearableFileInput

class ProcurementForm(forms.ModelForm):
    class Meta:
        model = Procurement
        fields = ('description', 'files', 'title')
        widgets = {
            'files': ClearableFileInput(attrs={'multiple': True}),
        }
        # widget is important to upload multiple files
