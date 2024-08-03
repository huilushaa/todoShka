from django.urls import path
from .views import ProjectTemplateView, ProjectDeleteView

urlpatterns = [
    path('projects/<int:user_pk>/', ProjectTemplateView.as_view(), name='project_template'),
    path('delete/<int:pk>', ProjectDeleteView.as_view(), name='project_delete'),
]