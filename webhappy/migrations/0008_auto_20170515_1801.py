# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhappy', '0007_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='cover',
            field=models.CharField(default='https://img.youtube.com/vi/wi9Oz75dvI0/0.jpg', max_length=150),
        ),
        migrations.AlterField(
            model_name='video',
            name='img',
            field=models.FileField(blank=True, upload_to='media/videos_cover'),
        ),
    ]
