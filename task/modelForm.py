from django import forms

from .models import task, taskAllocate

class addTask(forms.ModelForm):


    class Meta:
        model = task
        #exclude = ['code', 'addedBy', 'addedOn']
        fields = '__all__'

class addAllocateTask(forms.ModelForm):

    class Meta:
        model = taskAllocate
        fields = '__all__'