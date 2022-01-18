from django.forms import ModelForm

from .models import Pin
from boards.models import Board


class CreatePinForm(ModelForm):
    class Meta:
        model = Pin
        fields = ['board', 'title', 'image', 'description', 'link']

    def __init__(self, user, *args, **kwargs):
        super(CreatePinForm, self).__init__(*args, **kwargs)
        self.fields['board'].queryset = Board.objects.filter(user=user)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'