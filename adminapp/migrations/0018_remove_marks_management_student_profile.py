# Generated by Django 4.2.1 on 2023-05-31 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0017_student_management_marks_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks_management',
            name='Student_Profile',
        ),
    ]