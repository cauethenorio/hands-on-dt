# coding: utf-8

from modeltranslation.translator import translator, TranslationOptions

from . import models

class FaqTranslationOptions(TranslationOptions):
    fields = ('active', 'text', 'slug', 'answer')

translator.register(models.FrequentQuestion, FaqTranslationOptions)
