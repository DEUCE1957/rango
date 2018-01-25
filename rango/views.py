# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("""Rango says hey there partner! <br/>
	Be sure to check out the <a href="/rango/about">About page</a> 
	
	""")
	
def about(request):
	return HttpResponse("""Rango says here is the about page
	Lost? Return to the <a href = "/rango/">Home</a>
	""")
# Create your views here.
