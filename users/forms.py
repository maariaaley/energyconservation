from django import forms

from users.models import User

class UserForm(forms.Form):
    username = forms.CharField(label='User name', max_length=80)
    first_name = forms.CharField(label='First Name', max_length=80)
    last_name = forms.CharField(label='Last Name', max_length=80)
    phone_number = forms.IntegerField(label='Phone Number')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
    radio_buttons = forms.ChoiceField(
        choices=(
            ('is_landlord', "Landlord"),
            ('is_student', "Student")
        ),
        widget=forms.RadioSelect,
        label='Select your status'
    )