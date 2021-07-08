from django.contrib import admin
from django.contrib import admin
from custom_users.models import Uzer
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Uzer, UserAdmin)

