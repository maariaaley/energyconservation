from django.http import HttpResponse
from django.shortcuts import render
from controller import StudentForm

# Create your views here.
def create(request):
    return render(request, 'index.html', {})
