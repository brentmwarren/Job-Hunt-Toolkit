# Generated by Django 3.0 on 2019-12-03 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_hunt_toolkit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='date_applied',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='company_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='job_url',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='personal_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Checklick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checks', to='job_hunt_toolkit.Application')),
            ],
        ),
    ]
