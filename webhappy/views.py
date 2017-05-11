#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import MainPage, Slider

def index(request):
    index_page = MainPage.objects.all()
    slider = Slider.objects.all()
    return render(request, 'webhappy/index.html',{ 'index_page': index_page[0], 'slider': slider})