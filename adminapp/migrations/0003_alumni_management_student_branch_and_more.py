# Generated by Django 4.2.1 on 2023-05-25 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_learning_management_course_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni_management',
            name='Student_Branch',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='alumni_management',
            name='Student_Profile',
            field=models.FileField(null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='alumni_management',
            name='Student_Roll_No',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='thesis_management',
            name='Thesis_File',
            field=models.FileField(null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='thesis_management',
            name='Thesis_Name',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
