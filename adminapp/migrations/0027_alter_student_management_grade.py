# Generated by Django 4.2 on 2023-06-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0026_alter_student_management_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_management',
            name='Grade',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
