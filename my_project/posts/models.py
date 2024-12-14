from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=16)
    description = models.TextField(max_length=3000)  

    def __str__(self):
        return self.title  

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    text = models.TextField(max_length=2000)
    likes = models.PositiveIntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Comment by {self.user.username} on {self.created_at}"  


class New(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
