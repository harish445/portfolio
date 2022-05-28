from distutils.command.upload import upload
import email
from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    designation_two = models.CharField(max_length=200)
    bio = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    website = models.CharField(max_length=200)
    cv = models.FileField(upload_to='profile/cv/')
    icon = models.ImageField(upload_to='profile/', default='loc.png')
    iconname = models.CharField(max_length=200, default='iconname')
    
    def __str__(self):
        return self.name
    
class Skills(models.Model):
    icon = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
        
    
    