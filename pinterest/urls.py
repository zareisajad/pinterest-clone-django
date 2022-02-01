from django.urls import path

from .views import home, search

app_name = 'pinterest'

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
]