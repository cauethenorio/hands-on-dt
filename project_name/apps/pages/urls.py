# coding: utf-8

from django.conf.urls import patterns, include, url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(_(r'^perguntas-frequentes$'), views.FaqView.as_view(), name='faq'),
    url(_(r'^contato/'),
        include(patterns('',
            url(r'^$', views.ContactView.as_view(), name='index'),
            url(_(r'^obrigado$'), views.ContactThanksView.as_view(), name='thanks'),
        ), namespace='contact')
    ),
)