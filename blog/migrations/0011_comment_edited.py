# Generated by Django 3.2.4 on 2021-07-27 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_comment_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='edited',
            field=models.BooleanField(default=False),
        ),
    ]
