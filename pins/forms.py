from django.forms import ModelForm

from .models import Pin, Comment
from boards.models import Board


class CreatePinForm(ModelForm):
    class Meta:
        model = Pin
        fields = ['board', 'file', 'title', 'description', 'link']

    def __init__(self, user, *args, **kwargs):
        super(CreatePinForm, self).__init__(*args, **kwargs)
        self.fields['board'].queryset = Board.objects.filter(user=user)
        self.fields['title'].widget.attrs['placeholder'] = 'Add a Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Tell everyone what your pin is about..'
        self.fields['link'].widget.attrs['placeholder'] = 'Add a destination link'
        for visible in self.visible_fields():
            if visible.name == 'description':
                visible.field.widget.attrs['class'] = 'description-input border form-control'
            elif visible.name == 'board':
                visible.field.widget.attrs['class'] = 'board-input border form-control'
            else:
                visible.field.widget.attrs['class'] = 'form-control border rounded-pill'


class SaveToBoard(ModelForm):
    class Meta:
        model = Pin
        fields = ['board']

    def __init__(self, user, *args, **kwargs):
        super(SaveToBoard, self).__init__(*args, **kwargs)
        self.fields['board'].queryset = Board.objects.filter(user=user)
        for visible in self.visible_fields():
            if visible.name == 'board':
                visible.field.widget.attrs['class'] = 'board-input border form-control'


class EditPinForm(ModelForm):
    class Meta:
        model = Pin
        fields = ['board', 'title', 'description', 'link']

    def __init__(self, user, *args, **kwargs):
        super(EditPinForm, self).__init__(*args, **kwargs)
        self.fields['board'].queryset = Board.objects.filter(user=user)
        self.fields['title'].widget.attrs['placeholder'] = 'Add a Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Tell everyone what your pin is about..'
        self.fields['link'].widget.attrs['placeholder'] = 'Add a destination link'
        for visible in self.visible_fields():
            if visible.name == 'description':
                visible.field.widget.attrs['class'] = 'description-input border form-control'
            else:
                visible.field.widget.attrs['class'] = 'form-control border rounded-pill'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = 'Add comment'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control rounded-pill border'