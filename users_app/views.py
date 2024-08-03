from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, TemplateView, LogoutView
from .models import CustomUser
from .forms import RegistrationForm, LoginForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RegistrationCreateView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    model = CustomUser
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = CustomUser.objects.filter(username=username).first()
        if user is not None:
            print(f'User {username} found in the database.')
        return response


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('profile_update')

    def get_success_url(self):
        user = self.request.user
        return reverse_lazy('profile_update', kwargs={'pk': user.pk})


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class ProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'profile.html'

    def get_success_url(self):
        return reverse_lazy('profile_update', args=(self.object.id,))
