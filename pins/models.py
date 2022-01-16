from django.db import models

from accounts.models import User
from boards.models import Board


class Pin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pin_user')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='boards')
    image = models.ImageField(upload_to='pins')
    title = models.CharField(max_length=250)
    description = models.TextField()
    link = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)    