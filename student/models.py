from django.db import models
# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=80, default='Maria')
    last_name = models.CharField(max_length=80, default='Aley')
    age = models.IntegerField()
    email = models.CharField(max_length=80, default='maria@gmail.com')

