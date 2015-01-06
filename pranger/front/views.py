# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.mail import send_mail
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from braces.views import CanonicalSlugDetailMixin

from . import models


class HomeView(ListView):
    model = models.Website
    template_name = 'front/home.html'


class WebsiteView(CanonicalSlugDetailMixin, DetailView):
    model = models.Website
    template_name = 'front/website.html'
    context_object_name = 'site'


class InfoView(TemplateView):
    template_name = 'front/info.html'


class SubmissionView(CreateView):
    model = models.Submission
    fields = ['url', 'email', 'comment']
    template_name = 'front/submission.html'
    success_url = reverse_lazy('submission_thanks')

    def form_valid(self, form):
        handler = super(SubmissionView, self).form_valid(form)

        # Send notification email
        if settings.ADMINS:
            subject = '[passwortpranger] New Submission: %s' % self.object.url
            message = 'There is a new submission on Passwortpranger:\n\n%s%s' % (
                    settings.SITE_URL,
                    reverse('admin:front_submission_change', args=[self.object.pk])
            )
            sender = self.object.email or 'noreply@passwortpranger.ch'
            receivers = ['%s <%s>' % (admin[0], admin[1]) for admin in settings.ADMINS]
            send_mail(subject, message, sender, receivers, fail_silently=False)
        else:
            print('No admin e-mails found')

        return handler


class SubmissionThanksView(TemplateView):
    template_name = 'front/submission_thanks.html'
