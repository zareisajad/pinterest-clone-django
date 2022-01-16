from django.forms import ModelForm

from .models import Pin


class CreatePinForm(ModelForm):
    class Meta:
        model = Pin
        fields = ['board', 'title', 'image', 'description', 'link']

    def __init__(self, *args, **kwargs):
        super(CreatePinForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'