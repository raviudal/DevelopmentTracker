from django.urls import path
from . import views as task_view


urlpatterns = [
path('', task_view.index, name='index'),
path('task/', task_view.TaskListView.as_view(), name='task'),
#path('task/task', task_view.addtask, name='task'),
path('task/assignedTask', task_view.assignedTask, name='assignedTask'),
path('task/connectionDetails', task_view.connectionDetails, name='connectionDetails'),
path('task/addtask', task_view.addtask, name='addtask'),
path('task/AssignTask', task_view.assignedTask, name='allocateTask'),

path('task/<slug:pk>', task_view.addtask, name='task'),

]



