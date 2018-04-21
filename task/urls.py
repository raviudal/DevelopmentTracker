from django.urls import path
from . import views as task_view

urlpatterns = [
path('', task_view.index, name='index'),

]

