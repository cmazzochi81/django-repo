# Generated by Django 3.0.1 on 2020-01-19 01:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionitem', '0014_auto_20200113_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='endDate',
            field=models.DateTimeField(default=datetime.date(2020, 1, 25)),
        ),
        migrations.AlterField(
            model_name='auctionitem',
            name='startDate',
            field=models.DateTimeField(default=datetime.date(2020, 1, 18)),
        ),
    ]
