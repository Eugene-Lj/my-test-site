from django.db import models
from django.forms.models import modelform_factory

class Table(models.Model):
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    files = models.FileField(upload_to='uploads/', null=True)
    files2 = models.FileField(upload_to='uploads/', null=True, blank=True)
    
    '''def __str__(self):
        return self.title'''

'''TableForm = modelform_factory(Table)'''