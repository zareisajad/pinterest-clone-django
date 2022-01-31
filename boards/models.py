from django.db import models

from accounts.models import User


class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_user')
    title = models.CharField(max_length=250)
    pins = models.ManyToManyField('pins.Pin', related_name='pins', blank=True)
    cover = models.ImageField(upload_to='boards', default='boards/default.png')
    is_private = models.BooleanField(default=False)
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title