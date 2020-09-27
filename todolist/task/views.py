from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Task


# Create your views here.

def index(request):
    
    tasks = Task.objects.all()
    return render(request,'task/index.html',{'tasks' : tasks})



def add_todo(request):
    inputext = request.POST.get('q', None)
    if inputext is not None:
        title = Task(title=inputext)
        title.save()
    return HttpResponseRedirect('/')


def delete_todo(request, pk=None):
    if pk is not None:
        title = Task.objects.get(pk=pk)
        title.delete()
    return HttpResponseRedirect('/')

    


    
#pub_date