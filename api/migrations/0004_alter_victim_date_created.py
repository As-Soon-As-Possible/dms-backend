# Generated by Django 3.2.9 on 2021-11-24 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211124_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='victim',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 17, 21, 12, 582529)),
        ),
    ]
