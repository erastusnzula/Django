# Generated by Django 3.2.4 on 2021-07-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210701_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(verbose_name='Date Published'),
        ),
    ]
