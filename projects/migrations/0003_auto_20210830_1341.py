# Generated by Django 3.2.4 on 2021-08-30 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210830_1339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created_on'], 'verbose_name': 'Project', 'verbose_name_plural': 'Project'},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='added_on',
            new_name='created_on',
        ),
    ]