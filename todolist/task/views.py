from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Task


# Create your views here.

def index(request):
    
    tasks = Task.objects.all()
    return render(request,'task/index.html',{'tasks' : tasks})



def add_todo(request):
    inputext = request.POST.get('q', None)
    if inputext is not None:
        print(inputext)
    return HttpResponseRedirect('/')


    
