# Generated by Django 4.2.3 on 2023-07-13 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Kurs adını yazınız",
                        max_length=200,
                        unique=True,
                        verbose_name="Kurs Adı",
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("image", models.ImageField(upload_to="courses/%Y/%m/%d/")),
                ("date", models.DateTimeField(auto_now=True)),
                ("available", models.BooleanField(default=True)),
            ],
        ),
    ]
