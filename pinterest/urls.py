from django.urls import path

from .views import home

app_name = 'pinterest'

urlpatterns = [
    path('', home, name='home'),
]