#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import MainPage, Slider, Partner, Wwd, Video, How_to_help, Media, Media_images, About
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    about_page = About.objects.all()
    wwd = Wwd.objects.all()
    return render(request, 'webhappy/about.html', { 'index_page': index_page[0],
                                                   'partner': partner,
                                                    'about': about_page[0],
                                                    'wwd': wwd,
                                                   })
def what_we_do(request):
    index_page = MainPage.objects.all()
    partner = Partner.objects.order_by('number')
    obj = Media.objects.order_by('-date')

    paginator = Paginator(obj, 4)
    page = request.GET.get('page')

    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)

    index = documents.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    # My new page range
    page_range = list(paginator.page_range)
    page_range = page_range[start_index:end_index]
    return render(request, 'webhappy/what_we_do.html', { 'index_page': index_page[0],
                                                         'partner': partner,
                                                         'documents': documents,
                                                         'page_range': page_range,
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
    hth = How_to_help.objects.all()
    return render(request, 'webhappy/help.html', { 'index_page': index_page[0],
                                                   'partner': partner,
                                                   'hth': hth,
                                                   })

def contacts(request):
    index_page = MainPage.objects.all()
    partner = Partner.objects.order_by('number')

    return render(request, 'webhappy/contacts.html', { 'index_page': index_page[0],
                                                   'partner': partner,

                                                   })

def article(request, article_id):
    index_page = MainPage.objects.all()
    partner = Partner.objects.order_by('number')
    w_w_d = Media.objects.get(pk=article_id)
    images = w_w_d.images.all()
    print images
    return render(request, 'webhappy/article.html', {'index_page': index_page[0],
                                                  'partner': partner,
                                                  'media': w_w_d,
                                                     'images': images,
                                                  })