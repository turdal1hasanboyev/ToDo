from django.urls import path
from .views import index, add_todo, todo_detail, is_done

urlpatterns = [
    path('', index, name='main'),
    path('todo/', add_todo, name='todo'),
    path('todo/<int:pk>/', todo_detail, name="detail"),
    path('done/<int:pk>/', is_done, name="done"),
]