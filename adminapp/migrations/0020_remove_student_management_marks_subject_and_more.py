# Generated by Django 4.2 on 2023-06-01 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0019_student_management_att_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_management',
            name='Marks_Subject',
        ),
        migrations.AddField(
            model_name='student_management',
            name='Marks_Assignment',
            field=models.TextField(max_length=50, null=True),
        ),
    ]