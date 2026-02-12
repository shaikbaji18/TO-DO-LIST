from django.contrib import admin

# Register your models here.
from .models import TodoList, TodoItem

admin.site.register(TodoList)
admin.site.register(TodoItem)