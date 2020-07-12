from django.db import models

class ProcurementFiles(models.Model):
    file = models.FileField(upload_to='uploads/')

class Procurement(models.Model):
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    files = models.ManyToManyField(ProcurementFiles)
    
    def __str__(self):
        return self.title
'''class TableFeedFile(models.Model):
    #feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    files = models.ManyToManyField(TableFeed)
    #file = models.FileField(upload_to='uploads/')
    #files2 = models.FileField(upload_to='uploads/', null=True, blank=True)
    
class TableFeed(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feeds')
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    #files = models.ManyToManyField(TableFeedFile)
    file = models.FileField(upload_to='uploads/')

    '''

'''TableForm = modelform_factory(Table)'''

'''class ProcurementFiles(models.Model):
    procurement_id = int
    procurement_files = models.FileField()'''

'''class Feed(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='feeds')
    text=models.TextField(blank=False, max_length=500)
    files=models.ManyToManyField(FeedFile)

class FeedFile(models.Model):
    file = models.FileField(upload_to='uploads/')'''