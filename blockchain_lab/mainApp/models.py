from django.db import models

class SERVICES(models.Model):
    s_title = models.CharField(max_length=200)
    s_post = models.TextField()
    #s_image = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.s_title

class About(models.Model):
    a_title = models.CharField(max_length=200)
    a_post = models.TextField()
    a_image = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.a_title

class Portfolio(models.Model):
    p_title = models.CharField(max_length=200)
    p_post = models.TextField()
    p_image = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.p_title

class Team(models.Model):
    t_title = models.CharField(max_length=200)
    t_post = models.TextField()
    t_image = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.t_title