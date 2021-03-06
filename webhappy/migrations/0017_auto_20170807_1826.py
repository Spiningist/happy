# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-07 15:26
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('webhappy', '0016_auto_20170807_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='We_cares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='\u0414\u0435\u0442\u0441\u043a\u0438\u0439 \u0434\u043e\u043c', max_length=200)),
                ('text', tinymce.models.HTMLField(default='\u0421\u043b\u0435\u0434\u0443\u0435\u0442 \u043e\u0442\u043c\u0435\u0442\u0438\u0442\u044c, \u0447\u0442\u043e \u0431\u043b\u0430\u0433\u043e\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0444\u043e\u043d\u0434 \u043d\u0435 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u043e\u043c \u0437\u0430\u0449\u0438\u0442\u044b \u043b\u0438\u0447\u043d\u043e\u0433\u043e \u043a\u0430\u043f\u0438\u0442\u0430\u043b\u0430 \u0438\u043b\u0438 \u043d\u0430\u043b\u043e\u0433\u043e\u0432\u043e\u0439 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u0438. \u0421\u043b\u0435\u0434\u0443\u0435\u0442 \u043e\u0442\u043c\u0435\u0442\u0438\u0442\u044c, \u0447\u0442\u043e \u0431\u043b\u0430\u0433\u043e\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0444\u043e\u043d\u0434 \u043d\u0435 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u043e\u043c \u0437\u0430\u0449\u0438\u0442\u044b \u043b\u0438\u0447\u043d\u043e\u0433\u043e \u043a\u0430\u043f\u0438\u0442\u0430\u043b\u0430 \u0438\u043b\u0438 \u043d\u0430\u043b\u043e\u0433\u043e\u0432\u043e\u0439 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u0438. ', max_length=1000)),
                ('we_care_logo', models.ImageField(default='', upload_to='we_care')),
                ('number', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '\u041c\u044b \u043e\u043f\u0435\u043a\u0430\u0435\u043c',
                'verbose_name_plural': '\u041c\u044b \u043e\u043f\u0435\u043a\u0430\u0435\u043c',
            },
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': '\u041f\u0430\u0440\u0442\u043d\u0435\u0440', 'verbose_name_plural': '\u041f\u0430\u0440\u0442\u043d\u0435\u0440\u044b'},
        ),
    ]
