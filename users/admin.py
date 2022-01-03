from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm
from .models import User, Profile

#class CustomUserAdmin(UserAdmin):
#    add_form = UserForm

admin.site.register(User)
admin.site.register(Profile)