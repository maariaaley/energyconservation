from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import OneToOneField
from room.models import Room

label_choices = (
    ("1", "A"),
    ("2", "B"),
    ("3", "C"),
    ("4", "D"),
    ("5", "E"),
    ("6", "F"),
    ("7", "G"),
)
appliance_choice = (
    ("1", "LCD TV"),
    ("2", "Computer"),
    ("3", "Laptop"),
    ("4", "Lamp"),
    ("5", "Electric heater"),
    ("6", "Air conditioner"),
    ("7", "Mini-fridge"),
    ("8", "Fan"),
    ("9", "Extension cord"),
    ("10", "Smartphone charger"),
)
class Type(models.Model):
    type = models.CharField(max_length=20, choices=appliance_choice)
# Create your models here.
class Appliances(models.Model):
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    appliance_name = models.CharField(max_length=20)
    type = models.OneToOneField(Type, on_delete=models.CASCADE)
    label_class = models.CharField(max_length=1, choices=label_choices)
    energycomsuption = models.IntegerField() 
    
class Actions(models.Model):
    type = models.OneToOneField(Type, on_delete=models.CASCADE)
