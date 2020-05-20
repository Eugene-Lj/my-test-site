from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField()
    #image = models.ImageField()

    def __str__(self):
        return self.title
