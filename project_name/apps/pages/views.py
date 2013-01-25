# coding: utf-8

from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, 'index.jade')

def contact(request):
    return render(request, 'contact.jade')
