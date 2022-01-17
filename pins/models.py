import re
from unittest import removeResult
from urllib import request
from django.db import models

from accounts.models import User
from boards.models import Board


class Pin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pin_user')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='boards')
    image = models.ImageField(upload_to='pins')
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title