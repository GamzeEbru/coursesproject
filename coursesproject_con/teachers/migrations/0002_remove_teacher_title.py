# Generated by Django 4.2.3 on 2023-07-19 21:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="teacher",
            name="title",
        ),
    ]
