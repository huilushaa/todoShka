from django.contrib import admin
from django.urls import path, include
from users_app.views import RegistrationCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('priority_app.urls')),
    path('', include('project_app.urls')),
    path('', include('tag_app.urls')),
    path('', include('task_app.urls')),
    path('', include('users_app.urls')),
]
