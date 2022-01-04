from .models import *
from django import forms

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
class ApplianceForm(forms.ModelForm):
    appliance_name = forms.CharField(label='Appliance Name')
    label_class = forms.ChoiceField(choices=label_choices, label='Class')
    energycomsuption = forms.IntegerField(label='Energy Comsuption') 
    class Meta:
        model = Appliances
        exclude = []
