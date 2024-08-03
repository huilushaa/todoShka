from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_at', 'completed', 'due_date', 'project')
    list_filter = ('author', 'completed', 'due_date', 'project')
    search_fields = ('title', 'author__username', 'project__name')
    filter_horizontal = ('tags',)

admin.site.register(Task, TaskAdmin)