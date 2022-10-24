from django.shortcuts import redirect, render
from .models import Todo
from .form import Todoform
from django.shortcuts import get_object_or_404
# Create your views here.


def create_todo(request):

    form = Todoform()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = Todoform(request.POST)
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo')
    return render(request, './todo/createtodo.html', {'form': form})


def todo(request):
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)

    return render(request, './todo/todo.html', {"todos": todos})


def viewtodo(request, id):
    #todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo, id=id)
    return render(request, './todo/viewtodo.html', {"todo": todo})
