from django.forms import ModelForm

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
