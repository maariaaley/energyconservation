from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserForm
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = UserForm

admin.site.register(User, CustomUserAdmin)