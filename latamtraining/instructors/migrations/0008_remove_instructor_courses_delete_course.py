# Generated by Django 4.0.5 on 2022-07-10 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0007_alter_course_course'),
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
