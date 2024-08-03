from django.db import models
from users_app.models import CustomUser
from project_app.models import Project
from django.db.models import CASCADE
from tag_app.models import Tag
from django.conf import settings
from django.urls import reverse


class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=CASCADE, related_name='tasks', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tasks')

    def __str__(self):
        return self.title

    def comments(self):
        return self.comment_set.all()

    def get_absolute_url(self):
        return reverse('edit_task', kwargs={'project_id': self.project.id, 'pk': self.id})
