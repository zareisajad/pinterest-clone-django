from django.db import models
from mimetypes import guess_type

from accounts.models import User
from boards.models import Board


class Pin(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='pin_user'
    )
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name='boards'
    )
    file = models.FileField(upload_to='pins')
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_type(self):
        file_type = guess_type(self.file.url, strict=True)[0]
        # file_type might be ('video/mp4', None) or ('image/jpeg..etc', None)
        if 'video' in file_type:
            return 'video'
        elif 'image' in file_type:
            return 'image'

    
class Comment(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='all_comments')
    text = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} says {self.text}'
