# Generated by Django 3.2.4 on 2021-07-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20210712_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='items/thumbnails'),
        ),
    ]