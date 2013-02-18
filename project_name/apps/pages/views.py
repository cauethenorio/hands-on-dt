# coding: utf-8

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView


from . import forms, models
from ...libs.general import get_client_ip


def home(request):
    return render(request, 'index.jade')


class FaqView(ListView):
    template_name = 'faq.jade'
    context_object_name = 'questions'

    def get_queryset(self):
        return models.FrequentQuestion.objects.active()


class ContactView(FormView):
    template_name = 'contact/index.jade'
    form_class = forms.ContactMessageForm
    success_url = reverse_lazy('pages:contact:thanks')

    def form_valid(self, form):
        message = form.save(commit=False)
        message.ip = get_client_ip(self.request)
        message.user_agent = self.request.META.get('HTTP_USER_AGENT')
        message.save()

        form.send_email(self.request)
        return super(ContactView, self).form_valid(form)

class ContactThanksView(TemplateView):
    template_name = 'contact/thanks.jade'