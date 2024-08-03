from django import forms
from .models import Task


class EditTaskForm(forms.ModelForm):
    COMPLETED_CHOICES = [
        (True, 'Выполнено'),
        (False, 'Не выполнено')
    ]

    completed = forms.ChoiceField(
        choices=COMPLETED_CHOICES,
        widget=forms.RadioSelect(),
        label='Статус выполнения'
    )

    class Meta:
        model = Task
        fields = ['title', 'due_date', 'completed']
        labels = {
            'title': 'Название задачи',
            'due_date': 'Дедлайн',
            'completed': 'Статус выполнения',
        }
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date']
        labels = {
            'title': 'Название задачи',
            'due_date': 'Дедлайн',
        }
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }