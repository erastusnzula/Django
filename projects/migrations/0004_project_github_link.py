# Generated by Django 3.2.4 on 2021-08-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210830_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_link',
            field=models.CharField(default='', max_length=255),
        ),
    ]
