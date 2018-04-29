from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from task import modelForm
from .models import task
from django.contrib import messages
from django.views import generic
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django.db.models import Count


# Create your views here.
def index(request):
    template = 'task/index.html'
    ## filter for getting top 10 high priority tasks
    today_date = datetime.today()
    one_month_ago = today_date - relativedelta(months=2)
    not_clsed_task = task.objects.all().filter(plannedStartDate__gte = one_month_ago).filter(priority__exact='HIGH').exclude(status_id='CLS').order_by('plannedStartDate')[:20]


    ## filer for getting total work/tasks done for all clients
    #Blog.objects.values('entry__authors').annotate(entries=Count('entry'))
    tot = task.objects.values('project').distinct('project').annotate(Count('project'))

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

def assignedTask(request):
    context = {}
    if request.method == 'POST':
        print("+++++++++if POST If condition passed++++++++++")
        # Create a form instance and populate it with data from the request (binding):
        form = modelForm.addAllocateTask(request.POST)
        #myform = task(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #obj = form.save(commit=False)
            print(form)
            form.save()
            print('++++form is printed')
            messages.success(request, 'Form submission successful now go back to Tasks')
    else:
        form = modelForm.addAllocateTask()
    context['form'] = form

    return render(request, 'task/addAssignedTask.html', context)


def connectionDetails(request):
    context = {}
    return render(request, 'task/connectionDetails.html', context)

def addtask(request, pk=None):
    # If this is a POST request then process the Form data
    print(pk,'++++++++++')
    print("+++++++addTask is invoked++++++++++++")



    if request.method == 'POST' or pk != None:
        print("+++++++++if POST If condition passed++++++++++")
        # Create a form instance and populate it with data from the request (binding):
        myy = get_object_or_404(task, pk=pk)
        #form = modelForm.addTask(instance=myy)
        print(myy.name)
        myname = {'name': myy.name}
        form = modelForm.addTask(request.POST or None, instance=myy)

        #myform = task(request.POST)
        # Check if the form is valid:
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
            messages.success(request, 'Form submission successful now go back to Tasks')
            return HttpResponseRedirect('/task')


        # If this is a GET (or any other method) create the default form.
    else:
        print("+++++++++new form is created++++++++++", pk)
        form = modelForm.addTask()
        # myy = get_object_or_404(task, pk=pk)
        # form = modelForm.addTask(instance=myy)

    return render(request, 'task/addtask.html', {'form': form})

#This is a generic view
class TaskListView(generic.ListView):
    model = task
    context_object_name = 'task_list'
    queryset = task.objects.all()
    template_name = 'task/tasks.html'
    paginate_by = 40