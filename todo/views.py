from datetime import datetime
from email import message
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .models import Todo
from .form import Todoform
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.


def completed_byid(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed = not todo.completed
    todo.date_completed = datetime.now() if todo.completed else None
    todo.save()
    return redirect('todo')


@login_required
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todo')


@login_required
def completed(request):
    todos = Todo.objects.filter(
        user=request.user, completed=True)
    return render(request, './todo/completed.html', {'todos': todos})


def create_todo(request):
    message = ''
    form = Todoform()
    try:
        if request.method == 'POST':
            if request.user.is_authenticated:
                form = Todoform(request.POST)
                todo = form.save(commit=False)
                todo.user = request.user
                todo.date_completed = datetime.now() if todo.completed else None
                todo.save()
                return redirect('todo')
    except Exception as e:
        print(e)
        message = "資料錯誤"
    return render(request, './todo/createtodo.html', {'form': form, 'message': message})


def todo(request):
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)

    return render(request, './todo/todo.html', {"todos": todos})


def viewtodo(request, id):
    #todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'GET':
        form = Todoform(instance=todo)

    elif request.method == 'POST':
        if request.POST.get('update'):

            form = Todoform(request.POST, instance=todo)
            if form.is_valid():
                todo = form.save(commit=False)
                if todo.completed:
                    todo.date_completed = datetime.now()
                else:
                    todo.date_completed = None

            form.save()
        elif request.POST.get('delete'):
            todo.delete()
            return redirect('todo')
    return render(request, './todo/viewtodo.html', {"todo": todo, 'form': form})
