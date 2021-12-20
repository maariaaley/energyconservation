from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    pass #Add Django user fields to our model.
    #Custom fields
    phone_number = models.CharField(default='12345678', max_length=30)
    is_landlord = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
        
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)