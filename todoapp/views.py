from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.templates import loader

# Create your views here.

def index(request):
    task_list = Task.objects.all()
   # output = ','.join([q.task_name for q in task_list])
  # template = loader.get_template('todoapp/index.html')
   context = {

       'task_list':task_list,
   }
    #return HttpResponse(template.render(context, request))
    return render(request, 'todoapp/index.html', context)
  
def detail(request, task_id):
    return HttpResponse('This is task no. %s' % task_id)