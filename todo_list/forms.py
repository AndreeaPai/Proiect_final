from django import forms
from .models import Todo

class ListForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["added_date","text"]