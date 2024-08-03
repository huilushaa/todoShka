from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите свой email'}))
    birth_date = forms.DateField(widget=MyDateInput(attrs={
        'class': 'form-control', 'placeholder': 'Ваша дата рождения'}))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Выберите город'}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control-file'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'location', 'password1', 'password2', 'avatar')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class ProfileUpdateForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите свой никнейм'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите свой email'}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control py-4'}))
    bio = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Укажите информацию о себе. Например, ваши увлечения'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'bio')
