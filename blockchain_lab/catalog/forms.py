from django import forms
from catalog.models import Table

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('description', 'files', 'title', 'files2')
'''class FileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))'''
    