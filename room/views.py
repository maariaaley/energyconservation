from django.shortcuts import render, redirect

from users.models import Landlord, Student
from appliances.models import *
from .models import Room
from .forms import CreateRoomForm, UpdateRoomForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from appliances.forms import CreateActionForm

# Create your views here.


@login_required
def home(request):
    user = request.user
    if user.check_is_landlord():
        landlord = Landlord.objects.get(user_id = user.id)
        cuartos = Room.objects.all().filter(landlord_id = landlord.user_id)
        return render(request, 'room/rooms.html', {'cuartos': list(cuartos)})
    elif user.check_is_student():
        student = Student.objects.get(user_id = user.id)
        room = Room.objects.all().filter(student = student).first()
        appliances = Appliances.objects.all().filter(room = room)[0:5]
        actions = Actions.objects.all().filter(appliance_id__in=appliances.values_list('id'))[0:5]
        if actions == None:
            actions = list()
        return render(request, 'room/roomstudent.html', {'room': room, 'appliances': list(appliances), 'actions': list(actions)})
    else:
        return HttpResponse(200, user.check_is_student())
        


@login_required
def create(request):
    if request.method == "POST":
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            landlord = Landlord.objects.get(user_id = request.user.id)
            form.landlord = landlord
            form.save()
            return HttpResponseRedirect('/room/home')
        else:
            return render(request, 'room/createroom.html', {'form': form })
    else:
        form = CreateRoomForm()
        return render(request, 'room/createroom.html', {'form': form })
    
@login_required
def edit(request, id):
    if request.method == "POST":
        form = UpdateRoomForm(request.POST, instance=Room.objects.get(room_number=id))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/room/home')
        else:
            return render(request, 'room/editroom.html', {'form': form })
    else:
        form = UpdateRoomForm(instance=Room.objects.get(room_number=id))
        return render(request, 'room/editroom.html', {'form': form })


