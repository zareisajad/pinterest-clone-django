from xml.etree.ElementTree import PI
from django.contrib import admin

from .models import Pin, Comment

admin.site.register(Pin)
admin.site.register(Comment)
