# Generated by Django 4.2.1 on 2023-05-27 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_alter_student_management_alumni'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty_management',
            name='Status',
            field=models.TextField(default='pending', null=True),
        ),
    ]
