# Generated by Django 4.0.2 on 2022-05-26 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_student_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='comment',
        ),
    ]