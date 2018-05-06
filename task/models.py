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

APPLICATION_CHOICES = (
    ('QA', 'QA'),
    ('DEV', 'Development'),
    ('PROD', 'Production'),
)

VPN_CHOICES = (
    ('VPN', 'VPN'),
    ('Forticlient', 'Forticlient'),
    ('Sonicwall', 'Sonicwall'),
    ('Juniper', 'Juniper'),
    ('Windows', 'Windows')
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
    name = models.CharField(max_length=500, null=True, blank=True)
    product = models.ForeignKey('product', on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey('project', on_delete=models.SET_NULL, null=True)
    version = models.CharField(max_length=5, null=True, blank=True)
    taskType = models.CharField(max_length=5, choices=TASKTYPE_CHOICES, default='DEV', null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    crnNumber = models.CharField(max_length=100, null=True, blank=True)
    #attachedCRN = uploaded crn link
    #file = models.FileField(upload_to='docs/',null=True, blank=True)
    reportedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reportedOn = models.DateField(null=True, blank=True)
    plannedStartDate = models.DateField(null=True, blank=True)
    plannedEndDate = models.DateField(null=True, blank=True)
    revisedStartDate = models.DateField(null=True, blank=True)
    revisedEndDate = models.DateField(null=True, blank=True)
    estimatedHours = models.CharField(max_length=5, default=0, null=True, blank=True)
    priority = models.CharField(max_length=5, choices=TASK_PRIORITY, default='LOW', null=True, blank=True)
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
    status = models.ForeignKey('taskStatus', on_delete=models.SET_NULL, null=True)
    comment = models.TextField(null=True, blank=True)

    def return_abs_url(self):
        return reverse('assignedTask', args=[str(self.id)])


    class Meta:
        ordering = ['-id']

class upload(models.Model):
    name = models.CharField(max_length=20)
    file = models.FileField(upload_to='docs/')


class connectionDetails(models.Model):
    projectCode = models.ForeignKey('project', on_delete=models.SET_NULL, null=True, blank=True)    # - - DTGD[PRJ]
    application = models.CharField(max_length=15, choices=APPLICATION_CHOICES, null=True, blank=True)     # - - DTGD[APP - - QA / DEV / PRD]
    ip = models.CharField(max_length=15,null=True, blank=True)               # -  - VARCHAR[15]
    port = models.CharField(max_length=4,null=True, blank=True)             # - - VARCHAR[4]
    userIdAndPassword = models.TextField(max_length=500,null=True, blank=True)           # - - VARCHAR[check
    # password = models.TextField(max_length=50,null=True, blank=True)         # - - VARCHAR[check
    vpnApp = models.CharField(max_length=15, choices=VPN_CHOICES, null=True, blank=True)            # - - DTG[VPN - Forticlient, Sonicwall, Juniper, Windows
    vpnIp = models.CharField(max_length=15,null=True, blank=True)            # - - VARCHAR[15]
    vpnPort = models.CharField(max_length=6,null=True, blank=True)          # - - VARCHAR[6]
    vpnUserIdPassword = models.TextField(max_length=500,null=True, blank=True)        # - - VARCHAR(50)
    #vpnPassword = models.CharField(max_length=50,null=True, blank=True)      # - - VARCHAR(50)
    rdpIP = models.CharField(max_length=15,null=True, blank=True)            # - - VARCHAR(15)
    rdpUserIdAndPassword = models.TextField(max_length=500,null=True, blank=True)       # - - VARCHAR(50)[Total
    #rdpPassword1 = models.TextField(max_length=50,null=True, blank=True)     # - - VARCHAR(50)
    workspace = models.CharField(max_length=250,null=True, blank=True)        # - - VARCHAR(250)[Workspace
    #software = models.FileField(upload_to='docs/')
    comment = models.TextField(max_length=200,null=True, blank=True)

    def return_abs_url(self):
        return reverse('connectionDetails', args=[str(self.id)])

