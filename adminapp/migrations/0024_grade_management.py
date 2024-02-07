# Generated by Django 4.2 on 2023-06-01 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0023_student_management_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade_Management',
            fields=[
                ('Grade_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Student_Branch', models.TextField(max_length=100, null=True)),
                ('Student_Semester', models.TextField(max_length=100, null=True)),
                ('Student_Name', models.TextField(max_length=100)),
                ('Student_Roll_No', models.TextField(max_length=100)),
                ('Add_Marks', models.IntegerField(default=0, null=True)),
                ('Stu_Foregin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.student_management')),
            ],
            options={
                'db_table': 'grade_management',
            },
        ),
    ]