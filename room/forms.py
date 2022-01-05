from django import forms
from django.forms import fields
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, MonthPickerInput

from room.models import Room

class CreateRoomForm(forms.ModelForm):
    address = forms.CharField(label='Address', max_length=80)
    room_number = forms.CharField(label='Room number', max_length=80)
    square_meters = forms.IntegerField(label='Square meters')
    windows = forms.IntegerField(label='Windows quantity')
    
    class Meta:
        model = Room
        exclude = ['date']
    
    
class UpdateRoomForm(forms.ModelForm):
    address = forms.CharField(label='Address', max_length=80)
    square_meters = forms.IntegerField(label='Square meters')
    windows = forms.IntegerField(label='Windows quantity')

    class Meta:
        model = Room
        fields = ['address', 'square_meters', 'windows', 'is_insulated', 'has_bathroom']
        
        
class RegisterConsumptionForm(forms.Form):
    electricity = forms.IntegerField(label='Electricity (kWh)')
    gas = forms.IntegerField(label='Gas (kWh)')
    water = forms.IntegerField(label='Water (m^3)')
    date = forms.DateField(widget=MonthPickerInput())

