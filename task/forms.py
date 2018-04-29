from django import forms
from .models import product, project


# class addTask(forms.Form):
    # code = forms.CharField(max_length=100)
    # name = forms.CharField(max_length=500)
    # product = forms.ModelChoiceField(queryset=product.all(),  empty_label="(Nothing)")
    # project = forms.ModelChoiceField(queryset=project.all(),  empty_label="(Nothing)")
    # version = forms.CharField(max_length=5, null=True, blank=True)
    # taskType = forms.CharField(max_length=5, choices=TASKTYPE_CHOICES, default='DEV')
    # comment = forms.TextField(null=True, blank=True)
    # # attachedCRN = uploaded crn link
    # reportedBy = forms.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # reportedOn = forms.DateField(default=date.today(), null=True, blank=True)
    # plannedStartDate = forms.DateField(default=date.today(), null=True, blank=True)
    # plannedEndDate = forms.DateField(default=date.today(), null=True, blank=True)
    # revisedStartDate = forms.DateField(default=date.today(), null=True, blank=True)
    # revisedEndDate = forms.DateField(default=date.today(), null=True, blank=True)
    # estimatedHours = forms.IntegerField(max_length=3, default=0)
    # priority = forms.CharField(max_length=5, choices=TASK_PRIORITY, default='LOW')
    # actualStartDate = forms.DateField(default=date.today(), null=True, blank=True)
    # actualEndDate = forms.DateField(default=date.today(), null=True, blank=True)
    # status = forms.ForeignKey('taskStatus', on_delete=models.SET_NULL, null=True)
    # releasedDate = forms.DateField(null=True, blank=True)
    # releaseNote = forms.TextField(null=True, blank=True)
    # addedBy = forms.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_addedBy')
    # addedOn = forms.DateTimeField(default=datetime.now())