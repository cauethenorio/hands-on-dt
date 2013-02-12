# coding: utf-8

from django.conf.urls import patterns, include, url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(_(r'^perguntas-frequentes$'), views.FaqView.as_view(), name='faq'),
    url(_(r'^contato$'), views.ContactView.as_view(), name='contact'),
)