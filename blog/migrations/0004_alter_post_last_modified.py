# Generated by Django 3.2.4 on 2021-07-01 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_modified',
            field=models.DateTimeField(verbose_name='Date Updated'),
        ),
    ]
