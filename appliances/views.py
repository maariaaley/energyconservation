from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_GET, require_POST
from django.urls import reverse_lazy
from users.models import Student
from room.models import Room
from .forms import *
from .models import *
# Create your views here.

def home(request):
    user = request.user
    return None

        

def create(request, room_number):
    if request.method == "POST":
        form = ApplianceForm(request.POST)
        if form.is_valid():
            appliance = Appliances(
                room=Room.objects.get(room_number=room_number),
                label_class = form.cleaned_data['label_class'],
                appliance_name = form.cleaned_data['appliance_name'],
                type = Type.objects.get(type=form.cleaned_data['selecttype']),
                energycomsuption = form.cleaned_data['energycomsuption'],
            )
            appliance.save()
            return HttpResponseRedirect('/room/home')
        else:
            return render(request, 'appliances/create.html/', {'form': form, 'room_number':room_number})
    else:
        form = ApplianceForm()
        form.room_id = room_number
        form.room = Room.objects.get(room_number = room_number)
        return render(request, 'appliances/create.html', {'form': form, 'room_number': room_number})


@login_required
def create_action(request, room_number):
    if request.method == "POST":
        form = CreateActionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'room/home')
    else:
        appliances_options = Appliances.objects.all().filter(room = Room.objects.get(room_number=room_number))
        actions = Action_Appliance.objects.all().values_list('type', 'name')
        #return HttpResponse(appliances.values_list('id','appliance_name'))
        form = CreateActionForm()
        return render(request, 'appliances/createaction.html', {'form': form, 'room_number': room_number } )
    

def edit(request, room_number, appliance_id):
    return None