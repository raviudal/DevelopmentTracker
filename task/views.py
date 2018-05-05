from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from task import modelForm
from .models import task,taskAllocate,taskStatus, upload
from django.contrib import messages
from django.views import generic
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count


# Create your views here.
@login_required
def index(request):

    for group in request.user.groups.all():
        if group.name == 'Engineer':
            print('now redirect')
            return HttpResponseRedirect('task/assignedTask')

    template = 'task/index.html'
    ## filter for getting top 10 high priority tasks
    today_date = datetime.today()
    one_month_ago = today_date - relativedelta(months=2)
    not_clsed_task = task.objects.all().filter(plannedStartDate__gte = one_month_ago).filter(priority__exact='HIGH').exclude(status_id='CLS').order_by('plannedStartDate')[:20]

    tot = task.objects.filter(project='PSW').count()

    projects_stats_list = []
    for a in task.objects.raw("select t.code as code,t.project_id as projectCode, p.name as name, count(t.project_id) as total from task_task as t , task_project as p where t.project_id = p.code group by project_id"):
        # print(a.name, a.total)
        # print(task.objects.filter(status_id__exact='CLS').filter(project_id__exact=a.projectCode).count())
        cls = task.objects.filter(status_id__exact='CLS').filter(project_id__exact=a.projectCode).count()
        projects_stats_list.append(str(a.name + ' - ' + str(cls) + ' closed out of ' + str(a.total)))
    # .objects.filter(attribute__in=attributes).values('location').annotate(score=Sum('score')).order_by('-score')
    #values('project__name').annotate(Count('project'))
    print(projects_stats_list)
    context = {'not_closed_task':not_clsed_task, 'tot':tot, 'projects_stats_list':projects_stats_list}
    return render(request, template, context)

# def task(request):
#     context = {}
#     return render(request, 'task/tasks.html', context)
@login_required
def assignedTask(request):
    template = 'task/assignedTask.html'
    context = {}
    return render(request, template, context)

@login_required
def addAssignedTask(request, pk=None):
    is_engineer =False
    for group in request.user.groups.all():
        if group.name == 'Engineer':
            is_engineer = True

    context = {}
    context['is_engineer'] = is_engineer
    print(request.user, "++  inside the function")

    if request.method == 'POST' or pk != None:
        if pk == None:
            form = modelForm.addAllocateTask(request.POST)
            print(pk, "++  inside the function and pk is None")

        else:
            myy = get_object_or_404(taskAllocate, pk=pk)
            form = modelForm.addAllocateTask(request.POST or None, instance=myy)
            print(pk, "++  inside the function and pk is Nott None")

        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            if pk != None:
                update_status = task.objects.get(pk=form.cleaned_data['code'].code)
                update_status.status = taskStatus.objects.get(pk=form.cleaned_data['status'].code)
                update_status.save()
                form.save()

                # print('+++form.code ', form.cleaned_data['code'].status.code, '++ form.status', form.cleaned_data['status'].code)
            else:
                form.save(commit=False)
                # form.status = form.cleaned_data['code'].status.code
                #print('++++++taskStatus.objects.get(pk=form.cleaned_data[].status.code)',taskStatus.objects.get(pk=form.cleaned_data['code'].status.code))
                #form.status = taskStatus.objects.get(pk=form.cleaned_data['code'].status.code)
                form.save()
                print('++++form is saved')
            messages.success(request, 'Form submission successful now go back to Assingedtask')
            return HttpResponseRedirect(reverse('assignedTask'))

    else:
        form = modelForm.addAllocateTask()
    context['form'] = form

    return render(request, 'task/addAssignedTask.html', context)

@login_required
def connectionDetails(request):
    context = {}
    return render(request, 'task/connectionDetails.html', context)
@login_required
def addtask(request, pk=None):
    for group in request.user.groups.all():
        if group.name == 'Engineer':
            print('now redirect')
            return HttpResponseRedirect('task/assignedTask')

    print('++ inside the function')
    if request.method == 'POST' or pk != None:
        if pk == None:
            form = modelForm.addTask(request.POST)
        else:
            myy = get_object_or_404(task, pk=pk)
            form = modelForm.addTask(request.POST or None, instance=myy)
        print('++ before form validation')
        if form.is_valid():
            print('++ after form validation')
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #print(form)
            if pk:
                generated_key = pk
            else:
                product_id = task.return_product_id(str(form.cleaned_data['product']))
                project_id = task.return_project_id(str(form.cleaned_data['project']))
                count = task.return_count(my_product=product_id, my_project=project_id) + 1
                generated_key = str(product_id) + str(project_id) + str(count)

            obj = form.save(commit=False)
            # This if is just to put added on when new recored is created and do not update that field if that record is being updated
            if pk == None:
                obj.addedOn = datetime.now()
            obj.addedBy = request.user
            obj.code = generated_key
            obj.save()
            print('++Form saved++using key as =>', generated_key)
            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect('/task')


        # If this is a GET (or any other method) create the default form.
    else:
        print("+++++++++new form is created++++++++++", pk)
        form = modelForm.addTask()
        # myy = get_object_or_404(task, pk=pk)
        # form = modelForm.addTask(instance=myy)

    return render(request, 'task/addtask.html', {'form': form})



'''
def addtask(request, pk=None):
    print('++ inside the function')
    if request.method == 'POST' or pk != None:
        if pk == None:
            form = modelForm.addTask(request.POST)
        else:
            myy = get_object_or_404(task, pk=pk)
            form = modelForm.addTask(request.POST or None, instance=myy)
        print('++ before form validation')
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            print(form)
            if pk:
                generated_key = pk
            else:
                product_id = task.return_product_id(str(form.cleaned_data['product']))
                project_id = task.return_project_id(str(form.cleaned_data['project']))
                count = task.return_count(my_product=product_id, my_project=project_id) + 1
                generated_key = str(product_id) + str(project_id) + str(count)
            obj = form.save(commit=False)
            obj.code = generated_key
            obj.save()
            print('++Form saved++using key as =>', generated_key)
            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect('/task')


        # If this is a GET (or any other method) create the default form.
    else:
        print("+++++++++new form is created++++++++++", pk)
        form = modelForm.addTask()
        # myy = get_object_or_404(task, pk=pk)
        # form = modelForm.addTask(instance=myy)

    return render(request, 'task/addtask.html', {'form': form})

'''


#This is a generic view
class TaskListView(LoginRequiredMixin, generic.ListView):
    model = task
    context_object_name = 'task_list'
    queryset = task.objects.all()
    template_name = 'task/tasks.html'
    paginate_by = 40


class AssignedTaskListView(LoginRequiredMixin, generic.ListView):
    model = taskAllocate
    context_object_name = 'taskAllocate_list'
    queryset = taskAllocate.objects.all()
    template_name = 'task/assignedTask.html'
    paginate_by = 40


def upload(request):
    if request.method == 'POST':
        form = modelForm.UploadForm(request.POST, request.FILES)
        if form.is_valid():
            filename = form.save()
            print(form)
            print(filename)
            return render(request, 'task/testupload.html')
    else:
        form = modelForm.UploadForm()
    return render(request, 'task/testupload.html', {
        'form': form
    })