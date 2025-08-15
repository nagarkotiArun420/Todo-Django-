from django.shortcuts import render
from todo.models import Task



def home(request):
    return render(request, "home.html")

def manage(request):
    task = Task.objects.filter(is_completed=False).order_by('-updated_at')
    
    completed_tasks = Task.objects.filter(is_completed=True)
    
    
    
    context = {
        'tasks': task,
        'completed_tasks': completed_tasks
        
    }
    return render(request, "manage.html", context)