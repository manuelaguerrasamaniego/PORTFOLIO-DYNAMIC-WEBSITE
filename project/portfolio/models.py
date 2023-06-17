from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return self.name

class Blogs(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog',blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Internship(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    company=models.CharField(max_length=100)
    offer=models.TextField(default='Default offer message')
    start=models.TextField(default='')
    end=models.TextField(default='')
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company