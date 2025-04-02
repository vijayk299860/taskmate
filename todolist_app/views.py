from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Task added successfully')
            return redirect('todolist')
    else:
        form = TaskForm()
    
    all_tasks = TaskList.objects.filter(user=request.user)
    if request.user.is_superuser:
        all_tasks = TaskList.objects.all()
    paginator = Paginator(all_tasks, 10)
    page_number = request.GET.get('page')
    all_tasks = paginator.get_page(page_number)
    context = {
        'form': form,
        'welcome_text': 'Welcome to the Todo List App!',
        'all_tasks': all_tasks,
    }
    return render(request, 'todolist.html', context)

def edit_task(request, task_id):
    task = get_object_or_404(TaskList, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task modified successfully')
            return redirect('todolist')
    else:
        form = TaskForm(instance=task)
    
    context = {
        'form': form,
        'task': task
    }
    return render(request, 'edit_task.html', context)

def delete_task(request, task_id):
    task = get_object_or_404(TaskList, id=task_id)
    if request.user == task.user:
        task.delete()
        messages.success(request, 'Task deleted successfully')
    else:
        messages.error(request, 'You are not authorized to delete this task')
    return redirect('todolist')

def todolist_contact(request):
    context = {
        'contact_text': 'Welcome to the Contact US of Todo List App!' 
    }
    return render(request, 'contact.html', context)

def todolist_about(request):
    context = {
        'about_text': 'Welcome to the About US of Todo List App!' 
    }
    return render(request, 'about.html', context)

def index(request):
    context = {
        'home_text': 'Welcome to Todo List App!' 
    }
    return render(request, 'index.html', context)