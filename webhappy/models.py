#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from PIL import Image as Img
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class MainPage(models.Model):
    name_of_page = models.CharField(max_length=50, default='Главная страница и общая информация')
    phone_country = models.CharField(max_length=3, default='+7')
    phone_code = models.CharField(max_length=5, default='925')
    phone_number = models.CharField(max_length=10, default='346-07-27')
    email = models.CharField(max_length=30, default='fond-schastie@hotmail.com')
    adress = models.CharField(max_length=150, default='Адрес: г. Москва, ул. Тверская, 23')
    youtube = models.CharField(max_length=100, default='https://www.youtube.com/channel/UC20_z5bq_QyONSbVNtb3EVg')
    fb = models.CharField(max_length=100, default='https://www.facebook.com/fond.schastie/')
    insta = models.CharField(max_length=100, default='https://www.instagram.com/fond_schastie/')
    words = HTMLField(max_length=1000, default=' ')
    title = models.CharField(max_length=100, default=' ')
    name = models.CharField(max_length=100, default='Диана Менинбаева')
    photo = models.FileField(upload_to='media/CEO', default="")
    ps = HTMLField(max_length=1000, default=' ')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name_of_page) or u''

class Slider(models.Model):
    number = models.IntegerField(default=0)
    img = models.FileField(upload_to='media/slider')
    link = models.CharField(max_length=100, default='https://www.instagram.com/fond_schastie/')
    name = models.CharField(max_length=50, default='Слайдер №')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Partner(models.Model):
    name = models.CharField(max_length=50, default='Партнер №')
    link = models.CharField(max_length=100, default='https://www.instagram.com/fond_schastie/')
    img = models.FileField(upload_to='media/parner')
    number = models.IntegerField(default=0)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Wwd(models.Model):
    name = models.CharField(max_length=50, default='Что мы делаем?')
    img = models.FileField(upload_to='media/wwd_ico')
    text = HTMLField(max_length=1000, default='Задачей программ явлеяется целевые проекты и социальная поддержка населения')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Video(models.Model):
    name = models.CharField(max_length=50, default='Счастье is - ')
    img = models.FileField(upload_to='media/videos_cover', blank=True)
    link = models.CharField(max_length=150, default='https://www.youtube.com/channel/UC20_z5bq_QyONSbVNtb3EVg')
    cover = models.CharField(max_length=150, default='https://img.youtube.com/vi/wi9Oz75dvI0/0.jpg')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class How_to_help(models.Model):
    name = models.CharField(max_length=200, default='Благотворительная акция Банан')
    img = models.FileField(upload_to='media/how_to_help', blank=True)
    text = HTMLField(max_length=2000,
                     default='Задачей программ явлеяется целевые проекты и социальная поддержка населения')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Media(models.Model):
    date = models.DateTimeField(default='')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    name = models.CharField(max_length=200, default='Благотворительная акция Банан')
    cover = models.ImageField(upload_to='cover',default='')
    small_cover = models.ImageField(upload_to='cover',default='', blank=True, editable=False)
    short_text = HTMLField(max_length=2000,
                           default='Задачей программ явлеяется целевые проекты и социальная поддержка населения...')
    full_text = HTMLField(max_length=4000,
                           default='Задачей программ явлеяется целевые проекты и социальная поддержка населения...')

    def save(self, *args, **kwargs):
        if self.cover:
            image = Img.open(StringIO.StringIO(self.cover.read()))
            half_the_width = image.size[0] / 2
            half_the_height = image.size[1] / 2
            #image.thumbnail((403, 187), Img.ANTIALIAS)
            if image.size[0] >= image.size[1] and image.size[0]: #если ширина больше высоты
                rel = image.size[0] / 423
                new_height = image.size[1] / rel
                image.thumbnail((423, new_height), Img.ANTIALIAS)
                if new_height > 196 :
                    diff = new_height - 196
                    crop_y_begin = new_height / 2 - 98
                    crop_y_end = new_height / 2 + 98
                    #print 'size is ', image.size[0],' ', image.size[1]
                    #print 'crops are ', crop_y_begin, ' and ', crop_y_end
                    crop_image = image.crop((0, crop_y_begin, 423, crop_y_end))
                    #print 'new size is', crop_image.size[0], 'and ', crop_image.size[1]
                else:
                    diff =  196 - new_height
                    crop_y_begin = -diff / 2
                    crop_y_end = new_height + diff / 2
                    crop_image = image.crop((0, crop_y_begin, 423, crop_y_end))
            else:
                rel = image.size[0] / 423
                new_height = image.size[1] / rel
                image.thumbnail((423, new_height), Img.ANTIALIAS)

                if new_height >= 196 :
                    crop_y_begin = new_height / 2 - 98
                    crop_y_end = new_height / 2 + 98
                    # print 'size is ', image.size[0],' ', image.size[1]
                    # print 'crops are ', crop_y_begin, ' and ', crop_y_end
                    crop_image = image.crop((0, crop_y_begin, 423, crop_y_end))
                    # print 'new size is', crop_image.size[0], 'and ', crop_image.size[1]
                else:
                    print 'here2'
                    diff =  new_height - image.size[1]
                    end_height_crop = new_height + diff
                    crop_image = image.crop((0, diff, 423, end_height_crop))

            #crop_image.show()
            output = StringIO.StringIO()
            crop_image.save(output, format='JPEG', quality=100)
            output.seek(0)
            self.small_cover = InMemoryUploadedFile(output, 'ImageField', "small_%s.jpg" % self.cover.name,
                                                    'image/jpeg',
                                                    output.len, None)
        super(Media, self).save(*args, **kwargs)


    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Media_images(models.Model):
    vote_id = models.ForeignKey(Media, related_name='images')
    image_media = models.ImageField(upload_to='images', default='')
    small_image = models.ImageField(upload_to='images', default='', editable=False)

    def save(self, *args, **kwargs):
        if self.image_media:
            image = Img.open(StringIO.StringIO(self.image_media.read()))
            half_the_width = image.size[0] / 2
            half_the_height = image.size[1] / 2
            # image.thumbnail((403, 187), Img.ANTIALIAS)
            if image.size[0] >= image.size[1] and image.size[0]:  # если ширина больше высоты
                rel = image.size[0] / 405
                new_height = image.size[1] / rel
                image.thumbnail((405, new_height), Img.ANTIALIAS)
                if new_height > 208:
                    diff = new_height - 208
                    crop_y_begin = new_height / 2 - 104
                    crop_y_end = new_height / 2 + 104
                    # print 'size is ', image.size[0],' ', image.size[1]
                    # print 'crops are ', crop_y_begin, ' and ', crop_y_end
                    crop_image = image.crop((0, crop_y_begin, 405, crop_y_end))
                    # print 'new size is', crop_image.size[0], 'and ', crop_image.size[1]
                else:
                    diff = 208 - new_height
                    crop_y_begin = -diff / 2
                    crop_y_end = new_height + diff / 2
                    crop_image = image.crop((0, crop_y_begin, 405, crop_y_end))
            else:
                rel = image.size[0] / 405
                new_height = image.size[1] / rel
                image.thumbnail((405, new_height), Img.ANTIALIAS)

                if new_height >= 208:
                    crop_y_begin = new_height / 2 - 104
                    crop_y_end = new_height / 2 + 104
                    # print 'size is ', image.size[0],' ', image.size[1]
                    # print 'crops are ', crop_y_begin, ' and ', crop_y_end
                    crop_image = image.crop((0, crop_y_begin, 405, crop_y_end))
                    # print 'new size is', crop_image.size[0], 'and ', crop_image.size[1]
                else:
                    print 'here2'
                    diff = new_height - image.size[1]
                    end_height_crop = new_height + diff
                    crop_image = image.crop((0, diff, 405, end_height_crop))

                    # crop_image.show()
            output = StringIO.StringIO()
            crop_image.save(output, format='JPEG', quality=100)
            output.seek(0)
            self.small_image = InMemoryUploadedFile(output, 'ImageField', "small_%s.jpg" % self.image_media.name,
                                                    'image/jpeg',
                                                    output.len, None)
        super(Media_images, self).save(*args, **kwargs)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.image_media.name) or u''

