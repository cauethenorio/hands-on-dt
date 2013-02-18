# coding: utf-8

from modeltranslation.translator import translator, TranslationOptions

from . import models

class FaqTranslationOptions(TranslationOptions):
    fields = ('active', 'text', 'answer')

translator.register(models.FrequentQuestion, FaqTranslationOptions)
