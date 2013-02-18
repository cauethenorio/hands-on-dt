# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

from modeltranslation.translator import MultilingualManager
import django_extensions.db.fields as djext_fields



class ContactMessage(models.Model):

    sent_date = djext_fields.CreationDateTimeField(_(u'Data de envio'))

    name = models.CharField(_(u'Nome'), max_length=128)
    email = models.EmailField(_(u'Email'))
    phone = models.CharField(_(u'Telefone'), max_length=64, blank=True)

    message = models.TextField(_(u'Mensagem'))
    ip = models.IPAddressField(_(u'IP'))
    user_agent = models.CharField(_(u'User agent'), max_length=256)

    def __unicode__(self):
        return self.message if len(self.message) < 50 else u"%s..." % self.message[:50]
    __unicode__.admin_order_field = 'message'

    class Meta:
        ordering = ('-sent_date',)
        get_latest_by = 'sent_date'

        verbose_name = _(u'mensagem de contato')
        verbose_name_plural = _(u'mensagens de contato')


class FrequentQuestionModelManager(MultilingualManager):

    def active(self):
        return self.get_query_set().filter(active=True)

    def inactive(self):
        return self.get_query_set().filter(active=False)


class FrequentQuestion(models.Model):

    created_date = djext_fields.CreationDateTimeField(_(u'Data de criação'))
    modified_date = djext_fields.ModificationDateTimeField(_(u'Data de atualização'))
    active = models.BooleanField(_(u'Ativo'), default=True)

    sort_order = models.IntegerField(
        _(u'Posição'),
        default=0,
        help_text=_(u'A posição em que você gostaria que a questão fosse exibida.')
    )

    text = models.CharField(_(u'Texto'), max_length=256, blank=True)
    answer = models.TextField(_(u'Resposta'), blank=True)

    objects = FrequentQuestionModelManager()

    def __unicode__(self):
        return self.text_pt_br if self.text_pt_br else self.text_en
    __unicode__.admin_order_field = 'text'

    class Meta:
        ordering = ('sort_order',)
        get_latest_by = 'created_date'

        verbose_name = _(u'Pergunta frequente')
        verbose_name_plural = _(u'Perguntas frequentes')
