# Generated by Django 2.1.7 on 2019-04-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctporder',
            name='OrderSysID',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddIndex(
            model_name='ctporder',
            index=models.Index(fields=['OrderSysID'], name='api_ctporde_OrderSy_692581_idx'),
        ),
    ]
