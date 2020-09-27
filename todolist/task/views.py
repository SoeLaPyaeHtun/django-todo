from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Task
from .forms import TaskForm 


# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    context = {'tasks' : tasks, 'form':form}
    return render(request,'task/index.html', context)



def add_todo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
    return redirect('/')


def delete_todo(request, pk=None):
    if pk is not None:
        title = Task.objects.get(pk=pk)
        title.delete()
    return HttpResponseRedirect('/')


def edit_todo(request, pk=None):
    title = Task.objects.get(pk=pk)
    form = TaskForm(instance=title)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=title)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request,'task/edit.html',context)

# def edit(request, pk=None):
#     inputext = request.POST.get('q', None)
#     if pk is not None:
#         title = Task.objects.get(pk=pk)
#         title.title = inputext
#         title.save()
#     return HttpResponseRedirect('/')
