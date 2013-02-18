# coding: utf-8

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from crispy_forms import helper, layout, bootstrap

from . import models
from ...libs.form import ExtendedMetaModelForm

class ContactMessageForm(ExtendedMetaModelForm):

    class Meta:
        model = models.ContactMessage
        exclude = ('ip', 'user_agent')
        field_args = {
            'name': {
                '+error_messages': {
                    'required': _(u'Por favor entre com seu nome')
                }
            },
            'email': {
                '+error_messages': {
                    'required': _(u'Por favor entre com seu email')
                }
            },
            'message': {
                '+error_messages': {
                    'required': _(u'Por favor entre com a mensagem a ser enviada')
                }
            }
        }

    def __init__(self, *args, **kwargs):
        super(ContactMessageForm, self).__init__(*args, **kwargs)

        # formating the form (example in https://gist.github.com/maraujop/1838193)
        self.helper = helper.FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.render_unmentioned_fields = True
        #self.helper.html5_required = True

        self.helper.layout = layout.Layout(
            'name', 'email', 'phone',
            layout.Field('message', rows='3', css_class='input-xlarge'),
            bootstrap.FormActions(
                layout.Submit('submit', u'%s &raquo;' % _(u'Enviar mensagem'))
            )
        )

    def send_email(self, request):
        self.cleaned_data['request'] = request
        email_body = render_to_string('email/contact.jade', self.cleaned_data)

        email_message = EmailMessage(
            _(u'Mensagem enviada pelo formulário de contato'),
            email_body,
            '"%s" <%s>' % (self.cleaned_data['name'], self.cleaned_data['email']),
            [settings.CONTACT_FORM_TO_EMAIL])

        email_message.content_subtype = "html"  # Main content is now text/html

        try:
            email_message.send()
            return True
        except :
            return False