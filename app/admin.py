# importing modules and sub-modules
from django.contrib import admin
from .models import Event

# importing sub-modules for unregistration
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# Unregister your models here
admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.
admin.site.register(Event)