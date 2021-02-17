from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=50)
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    created_at = models.DateTimeField('CREATED DATE',auto_now_add=True)
    modified_at = models.DateTimeField('MODIFIED DATE',auto_now=True)
    def __str__(self):
        return self.postname
# Create your models here.
