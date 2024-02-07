# Generated by Django 4.2.1 on 2023-05-27 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence_Management',
            fields=[
                ('Attendence_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Student_Name', models.TextField(max_length=100)),
                ('Student_Roll', models.TextField(max_length=100)),
                ('Stu_Sem', models.TextField(max_length=100)),
                ('Stu_Branch', models.TextField(max_length=100)),
                ('Att_Status', models.TextField(max_length=20)),
            ],
            options={
                'db_table': 'attendance_management',
            },
        ),
    ]