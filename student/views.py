from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from student.forms import StudentForm
from student.models import Student

# Views related to student management
def create(request):
    print(request.method)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = Student(first_name=form.cleaned_data['first_name'],
                              last_name=form.cleaned_data['last_name'],
                              email=form.cleaned_data['email'],
                              phone_number=form.cleaned_data['phone_number']
                              )
            student.save()
            return HttpResponseRedirect('/student/create')
    else:
        student_form = StudentForm()
        return render(request, 'index.html', {'form': student_form})
