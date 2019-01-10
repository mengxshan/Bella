# Generated by Django 2.1.5 on 2019-01-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Command', models.CharField(max_length=100)),
                ('LogFile', models.CharField(max_length=100)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Command', models.CharField(max_length=100)),
                ('LogFile', models.CharField(max_length=100)),
                ('Crontab', models.CharField(max_length=100)),
                ('Activated', models.BooleanField()),
            ],
        ),
    ]
