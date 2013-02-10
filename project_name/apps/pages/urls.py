from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'faq$', views.FaqView.as_view(), name='faq'),
    url(r'contato$', views.ContactView.as_view(), name='contact'),
)