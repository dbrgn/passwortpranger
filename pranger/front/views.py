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
            scores["negative"]["MAX_LEN_16"] = -1

        elif website.pw_max_length == 1:
            scores["negative"]["MAX_LEN_10"] = -2
        elif website.pw_max_length == 3:
            scores["positive"]["MAX_LEN_UNLIMITED"] = 1

        if website.pw_alphabet_size_restricted:
            scores["negative"]["ALPHABET_LIMITED"] = -1

        if website.new_user_mail_has_own_password:
            scores["negative"]["PW_IN_REGISTRATION_MAIL"] = -1

        if website.remember_mail_has_new_password:
            scores["negative"]["NEW_PW_IN_REMEMBER_MAIL"] = -1

        if website.remember_mail_has_own_password:
            scores["negative"]["OWN_PW_IN_REMEMBER_MAIL"] = -3

        if website.tls == 0:
            scores["negative"]["TLS_NO"] = -2
        elif website.tls == 1:
            scores["negative"]["TLS_SOME"] = -1
        elif website.tls == 2:
            scores["hint"]["TLS_ALL"] = 0
        elif website.tls == 3:
            scores["positive"]["TLS_FORCED"] = 1

        if website.twofactor:
            scores["positive"]["TWO_FACTOR"] = 3

        if website.securitywidget:
            scores["positive"]["SECURITY_WIDGET"] = 1
        scores["sum"] = self.calculate(scores["positive"].itervalues(), scores["negative"].itervalues())
        context["scores"] = scores
        return context

    @staticmethod
    def calculate(positive, negative):
        score = sum(positive)
        if score > 6:
            score = 6
        score += sum(negative)
        if score < 0:
            score = 0
        return score


class InfoView(TemplateView):
    template_name = 'front/info.html'


