# Generated by Django 4.0.5 on 2022-06-24 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0003_course_instructor_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='courses',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
