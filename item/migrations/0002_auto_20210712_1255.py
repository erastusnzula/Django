# Generated by Django 3.2.4 on 2021-07-12 09:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 7, 12, 9, 54, 56, 623975, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='last_modified',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 7, 12, 9, 55, 9, 69028, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
