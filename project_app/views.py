from .models import Project
from django.views.generic import TemplateView, DetailView, DeleteView, UpdateView
from .forms import ProjectForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from users_app.models import CustomUser


class ProjectTemplateView(TemplateView):
    template_name = 'projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_pk = self.kwargs.get('user_pk')
        user = get_object_or_404(CustomUser, pk=user_pk)
        context['form'] = ProjectForm()
        context['projects'] = Project.objects.filter(author=self.request.user)
        context['user'] = user
        return context

    def post(self, request, *args, **kwargs):
        user_pk = self.kwargs.get('user_pk')
        user = get_object_or_404(CustomUser, pk=user_pk)
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = user
            form.save()
            return redirect('project_template', user_pk=user.pk)
        else:
            context = self.get_context_data()
            context['form'] = form
            return render(request, self.template_name, context)


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        project = self.object
        return reverse('project_template', kwargs={'user_pk': project.author.pk})
