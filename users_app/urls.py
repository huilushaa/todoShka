from django.urls import path, include
from .views import RegistrationCreateView, UserLoginView, LogoutView, ProfileUpdateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', RegistrationCreateView.as_view(), name='registration_template'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
