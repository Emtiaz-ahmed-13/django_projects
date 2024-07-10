from django.shortcuts import render, redirect, get_object_or_404
from . models import TaskModel
from . forms import TaskForm

def show_tasks(request):
    tasks=TaskModel.objects.filter(is_active=True
                                   )
    return render(request,'tasls/show_tasks.html',{'tasks':tasks})

def completed_tasks(request):
    tasks=TaskModel.objects.filter(is_active=True
                                   )
    return render(request,'tasks/completed_tasks.html',{'tasks':tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def edit_task(request,pk):
    task=get_object_or_404(TaskModel,pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

def delete_task(request,pk):
    task=get_object_or_404(TaskModel,pk=pk)
    task.is_active=False
    task.save()
    return redirect('show_tasks')

def complete_task(request,pk):
    task=get_object_or_404(TaskModel,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('show_tasks')