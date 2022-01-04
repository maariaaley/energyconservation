from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_GET, require_POST
from django.urls import reverse_lazy
from users.models import Student
from .forms import *
# Create your views here.

def home(request):
    user = request.user
    return None

        

def create(request, room_number):
    if request.method == "POST":
        form = ApplianceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/room/home')
        else:
            return render(request, 'appliances/create.html/', {'form': form})
    else:
        form = ApplianceForm()
        form.room = Room.objects.get(room_number = room_number)
        return render(request, 'appliances/create.html', {'form': form, 'room_number': room_number})


    


def edit(request, room_number, appliance_id):
    return None