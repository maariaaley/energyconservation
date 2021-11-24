from django import forms

class StudentForm(forms.Form):
  first_name = forms.CharField( label= 'first_name',max_length=80)
  last_name = forms.CharField(label= 'last_name', max_length=80)
  age = forms.IntegerField(label='age')
  email = forms.CharField(label= 'email',max_length=80)   