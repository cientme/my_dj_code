# Generated by Django 4.0.2 on 2022-05-26 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0004_student_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stuid',
            field=models.IntegerField(),
        ),
    ]
