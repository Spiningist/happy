#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

class MainPage(models.Model):
    name_of_page = models.CharField(max_length=50, default='Главная страница и общая информация')
    phone_country = models.CharField(max_length=3, default='+7')
    phone_code = models.CharField(max_length=5, default='925')
    phone_number = models.CharField(max_length=10, default='346-07-27')
    email = models.CharField(max_length=30, default='fond-schastie@hotmail.com')
    youtube = models.CharField(max_length=100, default='https://www.youtube.com/channel/UC20_z5bq_QyONSbVNtb3EVg')
    fb = models.CharField(max_length=100, default='https://www.facebook.com/fond.schastie/')
    insta = models.CharField(max_length=100, default='https://www.instagram.com/fond_schastie/')
    words = HTMLField(max_length=1000, default=' ')
    title = models.CharField(max_length=100, default=' ')
    name = models.CharField(max_length=100, default='Диана Менинбаева')
    photo = models.FileField(upload_to='media/CEO', default="")

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name_of_page) or u''

class Slider(models.Model):
    number = models.IntegerField(default=0)
    img = models.FileField(upload_to='media/slider')
    link = models.CharField(max_length=100, default='https://www.instagram.com/fond_schastie/')
    name = models.CharField(max_length=50, default='Слайдер №')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''