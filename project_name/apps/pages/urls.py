from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='pages.home'),
    url(r'contato$', views.contact, name='pages.contact'),
)