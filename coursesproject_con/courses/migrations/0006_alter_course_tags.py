# Generated by Django 4.2.3 on 2023-07-16 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0005_course_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="tags",
            field=models.ManyToManyField(blank=True, null=True, to="courses.tag"),
        ),
    ]
