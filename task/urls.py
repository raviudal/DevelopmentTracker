from django.urls import path
from . import views as task_view


urlpatterns = [
path('', task_view.index, name='index'),
path('task/', task_view.TaskListView.as_view(), name='task'),
path('task/assignedTask', task_view.AssignedTaskListView.as_view(), name='assignedTask'),
# path('task/assignedTask', task_view.assignedTask, name='assignedTask'),
path('task/assignedTask/<int:pk>', task_view.addAssignedTask, name='assignedTask'),
path('task/addAssignedTask', task_view.addAssignedTask, name='addAssignedTask'),
path('task/addtask', task_view.addtask, name='addtask'),
path('task/AssignTask', task_view.assignedTask, name='allocateTask'),

path('task/connectionDetails', task_view.ConnectionDetailListView.as_view(), name='connectionDetails'),
path('task/addConnectionDetails', task_view.addConnectionDetails, name='addConnectionDetails'),
path('task/connectionDetails/<int:pk>', task_view.addConnectionDetails, name='connectionDetails'),

path('task/<slug:pk>', task_view.addtask, name='task'),

path('upload', task_view.upload, name='upload'),


]



