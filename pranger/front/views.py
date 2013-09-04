# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from front import models


class HomeView(ListView):
    model = models.Website
    template_name = 'front/home.html'


class LegalView(TemplateView):
	template_name = 'front/legal.html'