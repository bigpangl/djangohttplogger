# Generated by Django 3.1 on 2020-11-17 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=32, verbose_name='Logger Name')),
                ('msg', models.TextField(default='', verbose_name='Msg')),
                ('args', models.TextField(default='', verbose_name='Args')),
                ('levelname', models.CharField(default='', max_length=8, verbose_name='Level Name')),
                ('levelno', models.CharField(default='', max_length=32, verbose_name='Level No')),
                ('pathname', models.CharField(default='', max_length=256, verbose_name='Path Name')),
                ('filename', models.CharField(default='', max_length=64, verbose_name='File Name')),
                ('module', models.CharField(default='', max_length=64, verbose_name='Module')),
                ('exc_info', models.TextField(default='', verbose_name='Exc Info')),
                ('exc_text', models.CharField(default='', max_length=32, verbose_name='Exc Text')),
                ('stack_info', models.CharField(default='', max_length=32, verbose_name='Stack Info')),
                ('lineno', models.CharField(default='', max_length=32, verbose_name='Line No')),
                ('funcname', models.CharField(default='', max_length=32, verbose_name='Func Name')),
                ('created', models.FloatField(default='', verbose_name='Created Timestmap')),
                ('msecs', models.FloatField(default='', verbose_name='Msecs')),
                ('relativeCreated', models.FloatField(default='', verbose_name='Relative Created')),
                ('thread', models.CharField(default='', max_length=32, verbose_name='Thread')),
                ('threadName', models.CharField(default='', max_length=32, verbose_name='Thread Name')),
                ('processName', models.CharField(default='', max_length=32, verbose_name='Process Name')),
                ('process', models.CharField(default='', max_length=32, verbose_name='Process')),
            ],
            options={
                'verbose_name': '日志中心',
                'verbose_name_plural': '日志中心',
            },
        ),
    ]