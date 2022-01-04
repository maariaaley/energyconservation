from django.forms.models import construct_instance
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
    ("LCD TV", "LCD TV"),
    ("Computer", "Computer"),
    ("Laptop", "Laptop"),
    ("Lamp", "Lamp"),
    ("Electric Heater", "Electric Heater"),
    ("Air Conditioner", "Air Conditioner"),
    ("Mini Fridge", "Mini Fridge"),
    ("Fan", "Fan"),
    ("Extension Cord", "Extension Cord"),
    ("Smarthphone Charger", "Smartphone Charger"),
)
class ApplianceForm(forms.Form):

    appliance_name = forms.CharField(label='Appliance Name')
    selecttype = forms.CharField(label='Type', widget=forms.Select(choices=appliance_choice))
    label_class = forms.ChoiceField(choices=label_choices, label='Class')
    energycomsuption = forms.IntegerField(label='Energy Comsuption') 
    class Meta:
        model = Appliances
        fields = ['appliance_name', 'label_class', 'energycomsuption', 'selecttype']



class CreateActionForm(forms.ModelForm):
    summary = forms.CharField(label='Summary', max_length=30)
    action = forms.CharField(label='Action Description', max_length=50)
    #appliance = forms.ChoiceField(label='Appliance', widget=forms.Select())
    #type_action = forms.ChoiceField(label='Type of Action', widget=forms.Select())
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['appliance'].choices = appliances_options
        #self.fields['type_action'].choices = actions_options
    
    
    class Meta:
        model = Actions
        exclude = []
    
    