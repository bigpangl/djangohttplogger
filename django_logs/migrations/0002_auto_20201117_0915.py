# Generated by Django 3.1.3 on 2020-11-17 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_logs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logs',
            old_name='processname',
            new_name='processName',
        ),
        migrations.RenameField(
            model_name='logs',
            old_name='relativecreated',
            new_name='relativeCreated',
        ),
        migrations.RenameField(
            model_name='logs',
            old_name='threadname',
            new_name='threadName',
        ),
    ]
