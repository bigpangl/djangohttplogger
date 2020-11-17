# Generated by Django 3.1.3 on 2020-11-16 09:45

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
                ('levelname', models.CharField(default='', max_length=8, verbose_name='Level Name')),
                ('levelno', models.CharField(default='', max_length=32, verbose_name='Level No')),
                ('thread', models.CharField(default='', max_length=32, verbose_name='Thread')),
                ('threadname', models.CharField(default='', max_length=32, verbose_name='Thread Name')),
                ('processname', models.CharField(default='', max_length=32, verbose_name='Process Name')),
                ('process', models.CharField(default='', max_length=32, verbose_name='Process')),
                ('asctime', models.DateTimeField(db_index=True, verbose_name='Asctime')),
                ('created', models.FloatField(default='', verbose_name='Created Timestmap')),
                ('msecs', models.FloatField(default='', verbose_name='Msecs')),
                ('relativecreated', models.FloatField(default='', verbose_name='Relative Created')),
                ('msg', models.TextField(default='', verbose_name='Msg')),
                ('pathname', models.CharField(default='', max_length=256, verbose_name='Path Name')),
                ('filename', models.CharField(default='', max_length=64, verbose_name='File Name')),
                ('module', models.CharField(default='', max_length=64, verbose_name='Module')),
                ('exc_info', models.TextField(default='', verbose_name='Exc Info')),
                ('exc_text', models.CharField(default='', max_length=32, verbose_name='Exc Text')),
                ('stack_info', models.CharField(default='', max_length=32, verbose_name='Stack Info')),
                ('lineno', models.CharField(default='', max_length=32, verbose_name='Line No')),
                ('funcname', models.CharField(default='', max_length=32, verbose_name='Func Name')),
                ('args', models.TextField(default='', verbose_name='Args')),
            ],
            options={
                'verbose_name': '日志中心',
                'verbose_name_plural': '日志中心',
            },
        ),
    ]
