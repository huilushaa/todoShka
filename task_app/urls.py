from django.urls import path
from .views import TasksTemplateView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path('project/<int:project_id>/tasks/', TasksTemplateView.as_view(), name='tasks_template'),
    path('project/<int:project_id>/tasks/add/', TaskCreateView.as_view(), name='add_task'),
    path('project/<int:project_id>/tasks/edit/<int:pk>/', TaskUpdateView.as_view(), name='edit_task'),
]