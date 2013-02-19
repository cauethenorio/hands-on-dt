# coding: utf-8

from django.contrib import admin
from django.utils.translation import get_language


# https://django-grappelli.readthedocs.org/en/latest/customization.html
class CommonAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"

    class Media:
        js = (
            'js/admin/jquery-no-conflict.js',
            'js/components/redactor/%s.js' % get_language().replace('-', '_'),
            'js/components/redactor/redactor.min.js',
            'js/admin/enable-redactor.js'
        )
        css = {
            'all': (
                'js/components/redactor/redactor.css',
            )
        }
