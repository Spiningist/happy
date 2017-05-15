#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import MainPage, Slider, Partner, Wwd, Video

def index(request):
    index_page = MainPage.objects.all()
    slider = Slider.objects.all()
    partner = Partner.objects.order_by('number')
    videos = Video.objects.all()
    wwd = Wwd.objects.all()
    return render(request, 'webhappy/index.html', { 'index_page': index_page[0],
                                                   'slider': slider,
                                                   'partner': partner,
                                                   'videos': videos,
                                                   'wwd': wwd,
                                                   })
def about(request):
    index_page = MainPage.objects.all()
    partner = Partner.objects.order_by('number')
    return render(request, 'webhappy/about.html', { 'index_page': index_page[0],
                                                   'partner': partner,
                                                   })
def what_we_do(request):
    index_page = MainPage.objects.all()
    partner = Partner.objects.order_by('number')
    return render(request, 'webhappy/what_we_do.html', { 'index_page': index_page[0],
                                                   'partner': partner,
                                                   })

def news(request):
    index_page = MainPage.objects.all()
    partner = Partner.objects.order_by('number')
    return render(request, 'webhappy/news.html', { 'index_page': index_page[0],
                                                   'partner': partner,
                                                   })
def we_cares(request):
    index_page = MainPage.objects.all()
    partner = Partner.objects.order_by('number')
    return render(request, 'webhappy/we_cares.html', { 'index_page': index_page[0],
                                                   'partner': partner,
                                                   })

def help(request):
    index_page = MainPage.objects.all()
    partner = Partner.objects.order_by('number')
    return render(request, 'webhappy/help.html', { 'index_page': index_page[0],
                                                   'partner': partner,
                                                   })

def contacts(request):
    index_page = MainPage.objects.all()
    partner = Partner.objects.order_by('number')

    return render(request, 'webhappy/contacts.html', { 'index_page': index_page[0],
                                                   'partner': partner,

                                                   })