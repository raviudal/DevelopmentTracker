from django import forms

from .models import task

class My(forms.ModelForm):


    class Meta:
        model = task
        exclude = ['comment']