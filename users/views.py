from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from users.forms import UserForm
from users.models import User
from django.contrib.auth.hashers import make_password 

# Create your views here.


def home(request):
    return render(request, 'users/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            is_landlord = 'is_landlord' == form.cleaned_data['radio_buttons']
            is_student = 'is_student' == form.cleaned_data['radio_buttons']
            user = User(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                password= make_password(form.cleaned_data['password']),
                is_landlord = is_landlord,
                is_student = is_student,
            )
            user.save()
            return HttpResponseRedirect('/signup')
    else:
        user_form = UserForm()
        return render(request, 'users/signup.html', {'form': user_form})