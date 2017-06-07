# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
#from .models import Weather

from django.http import JsonResponse
import json

# Create your views here.

def home(request):
	return render(request,"home.html")

def show_add_page(request):
	return render(request,"add_page.html")
