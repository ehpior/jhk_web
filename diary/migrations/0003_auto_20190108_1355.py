# Generated by Django 2.1.2 on 2019-01-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20190108_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ddate',
            name='pub_date',
            field=models.DateTimeField(verbose_name='published'),
        ),
    ]