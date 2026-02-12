from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
