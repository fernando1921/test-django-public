# Generated by Django 4.0.5 on 2022-07-10 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0011_remove_instructor_courses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Course',
            new_name='course',
        ),
    ]
