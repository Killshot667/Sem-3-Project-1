from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255)
    tag=models.CharField(max_length=255,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()

    def __str__(self):
        return self.title + " " + str(self.author)

    def get_absolute_url(self):
        return reverse('BlogDetail',args=str(self.id))