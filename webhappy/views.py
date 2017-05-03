#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import MainPage

def index(request):
    index_page = MainPage.objects.all()
    return render(request, 'webhappy/index.html',{ 'index_page': index_page[0]})