# Generated by Django 3.1.3 on 2020-11-19 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_http_logs', '0003_auto_20201119_1039'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='logs',
            index=models.Index(fields=['created', 'levelname'], name='django_http_created_183b45_idx'),
        ),
    ]
