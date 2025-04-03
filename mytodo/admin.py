from django.contrib import admin
from .models import ToDoItem  # Import your model

# Register the ToDoItem model
admin.site.register(ToDoItem)