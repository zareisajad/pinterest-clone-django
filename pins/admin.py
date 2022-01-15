from xml.etree.ElementTree import PI
from django.contrib import admin

from .models import Pin

admin.site.register(Pin)
