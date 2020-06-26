from django.db import models

class Table(models.Model):
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    files = models.FileField(upload_to='uploads/', null=True)
    files2 = models.FileField(upload_to='uploads/', null=True)
    
    def __str__(self):
        return self.title

'''class TableFile(models.Model):
    files = models.FileField(upload_to='uploads/', null=True)
    page = models.ForeignKey('Table', on_delete=models.DO_NOTHING)'''