from django import forms
from django.forms import fields

from room.models import Room

class CreateRoomForm(forms.ModelForm):
    address = forms.CharField(label='Address', max_length=80)
    room_number = forms.CharField(label='Room number', max_length=80)
    square_meters = forms.IntegerField(label='Square meters')
    windows = forms.IntegerField(label='Windows quantity')
    radio_buttons = forms.ChoiceField(
        choices=(
            ('is_insulated', "Yes"),
        ),
        widget=forms.RadioSelect,
        label='Is the room insulated?'
    ) 
    radio_buttons = forms.ChoiceField(
        choices=(
            ('true', "Yes"),
            ('false', "No")
        ),
        widget=forms.RadioSelect,
        label='Does the room have a bathroom?',
        required=False
    )
    
    class Meta:
        model = Room
        exclude = []
    
    
class UpdateRoomForm(forms.ModelForm):
    address = forms.CharField(label='Address', max_length=80)
    square_meters = forms.IntegerField(label='Square meters')
    windows = forms.IntegerField(label='Windows quantity')
    radio_buttons = forms.ChoiceField(
        choices=(
            ('is_insulated', "Yes"),
        ),
        widget=forms.RadioSelect,
        label='Is the room insulated?'
    ) 
    radio_buttons = forms.ChoiceField(
        choices=(
            ('true', "Yes"),
            ('false', "No")
        ),
        widget=forms.RadioSelect,
        label='Does the room have a bathroom?',
        required=False
    )
    
    class Meta:
        model = Room
        fields = ['address', 'square_meters', 'windows', 'is_insulated', 'has_bathroom']

