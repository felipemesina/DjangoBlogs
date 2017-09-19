# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a NEW form to create a NEW blog"
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request, number):
    print number
    return HttpResponse("placeholder to display blog {}".format(number))

def edit(request, number):
    print number
    return HttpResponse("placeholder to edit blog {}".format(number))

def destroy(request, number):
    return redirect('/blogs')
