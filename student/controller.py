from django import forms

class StudentForm(forms.Form):
  first_name = forms.CharField( label= 'first_name',max_length=80)
  last_name = forms.CharField(label= 'last_name', max_length=80)
  phone_number = forms.IntegerField(label='phone_number')
  email = forms.EmailField(label= 'email')   