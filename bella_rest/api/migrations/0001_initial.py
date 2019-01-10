# Generated by Django 2.1.5 on 2019-01-10 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CTPAccount',
            fields=[
                ('Name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('UserID', models.CharField(max_length=10)),
                ('Password', models.CharField(max_length=32)),
                ('BrokerID', models.CharField(max_length=100)),
                ('MdHost', models.CharField(max_length=100)),
                ('TdHost', models.CharField(max_length=100)),
                ('IsReal', models.BooleanField()),
            ],
        ),
    ]
