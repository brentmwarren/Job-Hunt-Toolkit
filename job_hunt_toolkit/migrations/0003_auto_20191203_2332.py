# Generated by Django 3.0 on 2019-12-03 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_hunt_toolkit', '0002_auto_20191203_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='application',
            name='job_url',
        ),
    ]
