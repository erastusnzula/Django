# Generated by Django 3.2.4 on 2021-07-12 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_item_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='thumbnail',
        ),
    ]