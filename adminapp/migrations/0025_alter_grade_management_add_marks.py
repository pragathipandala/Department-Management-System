# Generated by Django 4.2 on 2023-06-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0024_grade_management'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade_management',
            name='Add_Marks',
            field=models.FloatField(default=0, null=True),
        ),
    ]
