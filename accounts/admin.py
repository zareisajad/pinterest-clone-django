from django.contrib import admin

from .models import User, Profile, Follow

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Follow)