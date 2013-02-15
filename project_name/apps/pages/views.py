# coding: utf-8

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from . import forms, models


def home(request):
    return render(request, 'index.jade')


class FaqView(ListView):
    template_name = 'faq.jade'
    queryset = models.FrequentQuestion.objects.active()
    context_object_name = 'faqs'


class ContactView(FormView):
    template_name = 'contact.jade'
    form_class = forms.ContactMessageForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.save()
        form.send_email(self.request)

        return super(ContactView, self).form_valid(form)