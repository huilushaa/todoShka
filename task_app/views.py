from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView
from .models import Task, Project
from django.urls import reverse_lazy
from .forms import AddTaskForm, EditTaskForm
from .models import CustomUser


class TasksTemplateView(TemplateView):
    template_name = 'tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs['project_id']
        project = get_object_or_404(Project, id=project_id)
        user_pk = project.author.pk
        user = get_object_or_404(CustomUser, pk=user_pk)

        context['tasks'] = Task.objects.filter(project=project, author=user)
        context['project_title'] = project.name
        context['project_id'] = project_id
        context['user'] = user
        context['project'] = project
        return context


class TaskCreateView(CreateView):
    model = Task
    template_name = 'add_task.html'
    form_class = AddTaskForm

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['project_id']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tasks_template', kwargs={'project_id': self.kwargs['project_id']})


class TaskUpdateView(UpdateView):
    model = Task
    form_class = EditTaskForm
    template_name = 'task_update.html'

    def get_success_url(self):
        return reverse_lazy('tasks_template', kwargs={'project_id': self.kwargs['project_id']})
