# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from collections import defaultdict

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
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

    def get_context_data(self, **kwargs):
        context = super(WebsiteView, self).get_context_data(**kwargs)
        website = self.object
        scores = defaultdict(dict)

        if website.pw_max_length == 0:
            scores['negative']['MAX_LEN_16'] = -1
        elif website.pw_max_length == 1:
            scores['negative']['MAX_LEN_10'] = -2
        elif website.pw_max_length == 3:
            scores['positive']['MAX_LEN_UNLIMITED'] = 1

        if website.alphabet_limited:
            scores['negative']['ALPHABET_LIMITED'] = -1

        if website.eml_registration_plaintext:
            scores['negative']['PW_IN_REGISTRATION_MAIL'] = -1

        if website.eml_recovery_plaintext:
            scores['negative']['NEW_PW_IN_REMEMBER_MAIL'] = -1

        if website.eml_reminder_plaintext:
            scores['negative']['OWN_PW_IN_REMEMBER_MAIL'] = -3

        if website.tls == 0:
            scores['negative']['TLS_NO'] = -2
        elif website.tls == 1:
            scores['negative']['TLS_SOME'] = -1
        elif website.tls == 2:
            scores['hint']['TLS_ALL'] = 0
        elif website.tls == 3:
            scores['positive']['TLS_FORCED'] = 1

        if website.two_factor:
            scores['positive']['TWO_FACTOR'] = 3

        if website.pw_strength_indicator:
            scores['positive']['SECURITY_WIDGET'] = 1

        scores['sum'] = self.calculate(scores['positive'].itervalues(),
                                       scores['negative'].itervalues())

        context['scores'] = scores
        return context

    @staticmethod
    def calculate(positive, negative):
        sum_pos = 4 + sum(positive)
        if sum_pos > 6:
            sum_pos = 6
        sum_neg = sum(negative)
        if sum_neg < -6:
            sum_neg = -6
        total = sum_neg + sum_pos
        if total < 0:
            total = 0
        return {'positive': sum_pos, 'negative': sum_neg, 'total': total}


class InfoView(TemplateView):
    template_name = 'front/info.html'
