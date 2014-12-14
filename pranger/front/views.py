# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from django.core.urlresolvers import reverse_lazy
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


class SubmissionThanksView(TemplateView):
    template_name = 'front/submission_thanks.html'
