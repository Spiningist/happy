#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import MainPage, Slider, Partner, Wwd, Video
from django.shortcuts import render_to_response
from django.template import RequestContext

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

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