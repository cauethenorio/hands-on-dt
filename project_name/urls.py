# coding: utf-8

from django.conf import settings
from django.conf.urls import patterns, include, url, static
#from django.conf.urls.i18n import i18n_patterns

from .libs.i18n_routing import simple_i18n_patterns as i18n_patterns
from .apps.pages import urls as pages_urls

# Comment the next two lines to disable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^grappelli/', include('grappelli.urls')),
    # admin in a different URL
    url(r'^adm/', include(admin.site.urls)),

)

urlpatterns += i18n_patterns('',

    url(r'^', include(pages_urls, namespace='pages')),

    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

)

# serving uploaded files for development
if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
