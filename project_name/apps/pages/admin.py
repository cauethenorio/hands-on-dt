# coding: utf-8

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


class FaqAdmin(TranslationAdmin):

    search_fields = ('text_pt_br', 'text_en', 'answer')
    list_display = ('sort_order', 'active', '__unicode__')
    list_display_links = ('__unicode__',)
    list_editable = ('active', 'sort_order')
    list_filter = ('active_pt_br', 'active_en')


class ContactMessageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    date_hierarchy = 'sent_date'
    readonly_fields = ('sent_date', 'name', 'email', 'phone', 'message',
                       'ip', 'user_agent')
    search_fields = ('name', 'email', 'phone', 'message', 'ip')
    list_display = ('sent_date', 'ip', 'name', 'email', '__unicode__')
    list_display_links = ('__unicode__',)


admin.site.register(models.FrequentQuestion, FaqAdmin)
admin.site.register(models.ContactMessage, ContactMessageAdmin)