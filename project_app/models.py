from django.db import models
from django.db.models import CASCADE
from users_app.models import CustomUser


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser, on_delete=CASCADE, related_name='projects', default=1)

    def __str__(self):
        return self.name