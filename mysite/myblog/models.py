from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=50)
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    def __str__(self):
        return self.postname
# Create your models here.
