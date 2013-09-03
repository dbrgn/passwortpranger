# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic.base import View, TemplateView


class HomeView(TemplateView):
    template_name = 'front/home.html'
