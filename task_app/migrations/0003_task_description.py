# Generated by Django 5.0.6 on 2024-07-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task_app", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="description",
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
