from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import TodoList, TodoItem

def home(request):
    lists = TodoList.objects.all()
    return render(request, 'home.html', {'lists': lists})

def list_detail(request, list_id):
    todo_list = get_object_or_404(TodoList, id=list_id)
    items = todo_list.items.all()
    return render(request, 'list_detail.html', {'todo_list': todo_list, 'items': items})

def add_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            TodoList.objects.create(name=name)
        return redirect('home')
    return render(request, 'add_list.html')

def delete_list(request, list_id):
    todo_list = get_object_or_404(TodoList, id=list_id)
    if request.method == 'POST':
        todo_list.delete()
    return redirect('home')

def add_item(request, list_id):
    todo_list = get_object_or_404(TodoList, id=list_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            TodoItem.objects.create(list=todo_list, name=name)
    return redirect('list_detail', list_id=list_id)

def delete_item(request, item_id):
    item = get_object_or_404(TodoItem, id=item_id)
    list_id = item.list.id
    if request.method == 'POST':
        item.delete()
    return redirect('list_detail', list_id=list_id)

def toggle_item(request, item_id):
    item = get_object_or_404(TodoItem, id=item_id)
    if request.method == 'POST':
        item.is_active = not item.is_active
        item.save()
    return redirect('list_detail', list_id=item.list.id)


