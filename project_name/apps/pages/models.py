# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel


class ContactMessage(models.Model):

    sent_date = models.DateTimeField(
        _('Data de envio'),
        editable=False,
        auto_now_add=True
    )

    name = models.CharField(_('Nome'), max_length=128)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Telefone'), max_length=64, blank=True)

    message = models.TextField(_('Mensagem'))

    class Meta:
        verbose_name = _('mensagem de contato')
        verbose_name_plural = _('mensagens de contato')

