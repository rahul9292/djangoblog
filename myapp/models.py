from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.
class Postmodels(models.Model):
    title= models.CharField(max_length=30)
    content =models.CharField(max_length=1000)
    date_created=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
    
class messagebox(models.Model):
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    datetime_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.author.username} at {self.datetime_sent}"
    

    

        




