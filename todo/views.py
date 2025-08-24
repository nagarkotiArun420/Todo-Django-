from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from todo.models import Task
from django.contrib import messages

# Create your views here.



def addTask(request):
     task = request.POST.get('task')
     if not task:
        messages.error(request, "Task cannot be empty!")   
        return redirect('manage')  
     else:
        Task.objects.create(task = task)
        return redirect('manage')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('manage')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('manage')

def update_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method =='POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('manage')
        
    else:
        context= {
            'get_task':get_task,    
            
        } 
        return render(request,'update_task.html',context)
    
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('manage')
    