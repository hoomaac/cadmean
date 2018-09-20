# Generated by Django 2.1.1 on 2018-09-20 08:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 20, 8, 36, 30, 278136, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='joined_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 8, 36, 30, 276256, tzinfo=utc)),
        ),
    ]
