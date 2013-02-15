# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

from modeltranslation.translator import MultilingualManager
import django_extensions.db.fields as djext_fields



class ContactMessage(models.Model):

    sent_date = djext_fields.CreationDateTimeField(_('Data de envio'))

    name = models.CharField(_('Nome'), max_length=128)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Telefone'), max_length=64, blank=True)

    message = models.TextField(_('Mensagem'))

    class Meta:
        verbose_name = _('mensagem de contato')
        verbose_name_plural = _('mensagens de contato')


class FrequentQuestionModelManager(MultilingualManager):

    def active(self):
        return self.get_query_set().filter(active=True)

    def inactive(self):
        return self.get_query_set().filter(active=False)


class FrequentQuestion(models.Model):

    created_date = djext_fields.CreationDateTimeField(_('Data de criação'))
    modified_date = djext_fields.ModificationDateTimeField(_('Data de atualização'))
    active = models.BooleanField(_('Ativo'), default=True)

    sort_order = models.IntegerField(
        _('Posição'),
        default=0,
        help_text=_('A posição em que você gostaria que a questão fosse exibida.')
    )

    text = models.CharField(_('Texto'), max_length=256)
    slug = djext_fields.AutoSlugField(_('slug'), max_length=256, populate_from='text')
    answer = models.CharField(_('Resposta'), max_length=1024)

    objects = FrequentQuestionModelManager()

    class Meta:
        verbose_name = _('Pergunta frequente')
        verbose_name_plural = _('Perguntas frequentes')
