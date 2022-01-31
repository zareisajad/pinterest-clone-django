from django.forms import ModelForm
from django import forms

from .models import Board


class CreateBoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'is_private']

    def __init__(self, *args, **kwargs):
        super(CreateBoardForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Like "Places to Go" or "Recipes to Make"'
        for visible in self.visible_fields():
            if visible.name == 'title':
                visible.field.widget.attrs['class'] = 'form-control border rounded-pill p-2 mt-1'
            else:
                visible.field.widget.attrs['class'] = 'form-check-input mt-1 private-checkbox'


class EditBoardForm(ModelForm):
    cover = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Board
        fields = ['title', 'is_private', 'description', 'cover']

    def __init__(self, *args, **kwargs):
        super(EditBoardForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Like "Places to Go" or "Recipes to Make"'
        self.fields['description'].widget.attrs['placeholder'] = 'add description for this board'

        for visible in self.visible_fields():
            if visible.name == 'title':
                visible.field.widget.attrs['class'] = 'form-control border rounded-pill p-2 mt-1'
            if visible.name == 'is_private':
                visible.field.widget.attrs['class'] = 'form-check-input mt-1 private-checkbox'
            else:
                visible.field.widget.attrs['class'] = 'form-control border rounded-pill p-2 mt-1'

