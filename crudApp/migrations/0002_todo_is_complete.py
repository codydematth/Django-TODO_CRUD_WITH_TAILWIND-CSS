# Generated by Django 4.1.3 on 2022-11-18 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crudApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="is_complete",
            field=models.BooleanField(default=False),
        ),
    ]
