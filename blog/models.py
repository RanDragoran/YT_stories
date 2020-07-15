from django.db import models

class blog(models.Model):
    blogTitle = models.CharField(max_length=200)
    blogContent = models.TextField()
    blogDate = models.DateTimeField()
    blogWriter = models.CharField(max_length=100)
