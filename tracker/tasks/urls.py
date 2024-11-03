from django.urls import path, include
from .views import TaskListView, TaskDetailView

urlpatterns = [
    path('tasks/', TaskListView.as_view()),
    path('detail-task/<int:pk>', TaskDetailView.as_view()),
]
