from django.shortcuts import render, redirect, get_object_or_404
from .form import TodoForm
from .models import Todo


def index(request):
    query = request.GET.get('query')

    objects = Todo.objects.all().order_by('-id')

    if query:
        objects = objects.filter(title__icontains=query)

    context = {
        "objects": objects
    }

    return render(request, 'index.html', context)


def add_todo(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect('/')
    
    context = {
        "form": form
    }

    return render(request, 'todo.html', context)

def todo_detail(request, pk):  # bu funksiya ham ko'rish uchun, ham o'zgartirish uchun ishlaydi!
    todo = get_object_or_404(Todo, id=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()

        return redirect('/')

    context = {
        "form": form
    }

    return render(request, 'todo.html', context)

def is_done(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    if todo.is_done:
        todo.is_done = False
    else:
        todo.is_done = True
    todo.save()
    
    return redirect('/')
