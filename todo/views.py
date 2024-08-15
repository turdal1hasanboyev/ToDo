from django.shortcuts import render, redirect, get_object_or_404

from todo.form import TodoForm
from todo.models import Todo


def index(request):
    query = request.GET.get('query')

    objects = Todo.objects.all().order_by('id')

    if query:
        objects = objects.filter(title__icontains=query)

    return render(request, 'index.html', {"objects": objects})

def add_todo(request):
    form = TodoForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('main')
    
    return render(request, 'todo.html', {"form": form})

def todo_detail(request, pk):  # bu funksiya ham ko'rish uchun, ham o'zgartirish uchun ishlaydi!
    todo = get_object_or_404(Todo, id=pk)
    
    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid():
        form.save()

        return redirect('main')

    return render(request, 'todo.html', {"form": form})

def is_done(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    
    if todo.is_done:
        todo.is_done = False
        
    else:
        todo.is_done = True
        
    todo.save()
    
    return redirect('main')
