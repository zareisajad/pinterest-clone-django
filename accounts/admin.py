from django.contrib import admin

from .models import User, Profile

admin.site.register(User)
admin.site.register(Profile)