from django.urls import path, include
from .views import TaskListView

urlpatterns = [
    path('tasks/', TaskListView.as_view()),
]
