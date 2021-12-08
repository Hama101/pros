from django.db import models

# Create your models here.


class Profile(models.Model):
    choices = [
        ('male', 'male'),
        ('female', 'female'),
    ]

    CIN = models.IntegerField(blank=True, null=True , unique=True)
    name = models.CharField(max_length=200 , blank=True, null=True , unique=True)
    image = models.ImageField(upload_to='portfolio/images/' ,  blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    small_about = models.CharField(max_length=200 ,  blank=True, null=True)
    phone = models.CharField(max_length=20 ,  blank=True, null=True)
    email = models.CharField(max_length=200 ,  blank=True, null=True)
    gender = models.CharField(max_length=10 , choices=choices ,  blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"