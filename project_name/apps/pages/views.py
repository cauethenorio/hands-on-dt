# coding: utf-8

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from . import forms


def home(request):
    return render(request, 'index.jade')

class FaqView(ListView):
    template_name = 'faq.jade'


class ContactView(FormView):
    template_name = 'contact.jade'
    form_class = forms.ContactMessageForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # needed to print user-agent/ip in email body
        form.cleaned_data['request'] = self.request

        form.save()
        form.send_email()

        return super(ContactView, self).form_valid(form)