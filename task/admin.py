from django.contrib import admin
from .models import product,project,task, taskStatus


my_models = [
    project,
    product,
    task,
    taskStatus
]



admin.site.register(my_models)