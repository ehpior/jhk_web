# Generated by Django 2.1.2 on 2019-01-08 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_auto_20190108_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='ddiary',
            name='dtime',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
    ]
