# Generated by Django 4.0.2 on 2022-05-26 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='Not available', max_length=40),
        ),
    ]
