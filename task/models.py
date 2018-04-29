from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
from dateutil.relativedelta import relativedelta


# Choice fields used by models
TASKTYPE_CHOICES = (
    ('DEV', 'Development'),
    ('ISS', 'Issue.'),
    ('REP', 'Report'),
)

TASK_PRIORITY = (
    ('HIGH', 'High'),
    ('LOW', 'Low'),
    ('TRI', 'Trivial'),
)

# Models Definations here.
class product(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class project(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class taskStatus(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class task(models.Model):
    
    code = models.CharField(max_length=100, primary_key=True)
    name =    models.CharField(max_length=500, null=True, blank=True)
    product = models.ForeignKey('product', on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey('project', on_delete=models.SET_NULL, null=True)
    version = models.CharField(max_length=5, null=True, blank=True)
    taskType = models.CharField(max_length=5, choices=TASKTYPE_CHOICES, default='DEV')
    comment = models.TextField(null=True, blank=True)
    crnNumber = models.CharField(max_length=100, null=True, blank=True)
    #attachedCRN = uploaded crn link
    reportedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reportedOn = models.DateField(null=True, blank=True)
    plannedStartDate = models.DateField(null=True, blank=True)
    plannedEndDate = models.DateField(null=True, blank=True)
    revisedStartDate = models.DateField(null=True, blank=True)
    revisedEndDate = models.DateField(null=True, blank=True)
    estimatedHours = models.IntegerField(max_length=3, default=0)
    priority = models.CharField(max_length=5, choices=TASK_PRIORITY, default='LOW')
    actualStartDate = models.DateField(null=True, blank=True)
    actualEndDate = models.DateField(null=True, blank=True)
    status = models.ForeignKey('taskStatus', on_delete=models.SET_NULL, null=True)
    releasedDate = models.DateField( null=True, blank=True)
    releaseNote = models.TextField(null=True, blank=True)
    addedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_addedBy', blank=True)
    addedOn  = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    def __str__(self):
        return self.code

    def return_count(my_product='NOW', my_project = 'BTM'):
        return  task.objects.filter(product_id =my_product, project_id= my_project).count()
    def return_project_id(project_name):
        return  project.objects.filter(name=project_name).first().code
    def return_product_id(product_name):
        return  product.objects.filter(name=product_name).first().code

    def return_abs_url(self):
        return reverse('task', args=[str(self.code)])


    def return_top_10_high_works(self):
        today_date = datetime.today()
        one_month_ago = today_date - relativedelta(months=1)
        return task.objects.filter(plannedStartDate__gte = one_month_ago )[20]


    class Meta:
        ordering = ['priority', 'addedOn']

class taskAllocate(models.Model):
    code = models.ForeignKey('task', on_delete=models.SET_NULL, null=True)
    assignedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='%(class)s_assignedBy')
    assignedTo = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    assignedOn = models.DateField(null=True, blank=True)
    startedOn = models.DateField(null=True, blank=True)
    finisedOn = models.DateField(null=True, blank=True)
    estimatedFinishDate = models.DateField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)