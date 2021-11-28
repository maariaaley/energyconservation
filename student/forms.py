from django import forms

class StudentForm(forms.Form):
  first_name = forms.CharField( label= 'First Name',max_length=80)
  last_name = forms.CharField(label= 'Last Name', max_length=80)
  phone_number = forms.IntegerField(label='Phone Number')
  email = forms.EmailField(label= 'Email')