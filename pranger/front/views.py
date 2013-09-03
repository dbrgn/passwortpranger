# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic.base import View, TemplateView


class HomeView(TemplateView):
    template_name = 'front/home.html'


class LoginView(View):
    """Redirect to real login view."""

    def get(self, request, *args, **kwargs):
        url = reverse('socialauth_begin', args=('google-oauth2',))
        # Keep query string (especially "next" parameter)
        full_url = '%s?%s' % (url, request.GET.urlencode())
        return redirect(full_url)


class LoginSuccessfulView(View):
    """Redirect to home view, show a message."""

    def get(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'You have successfully logged in.')
        return redirect('home')


class LogoutView(View):
    """Log the user out, redirect to home view, show a message."""

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'You have successfully logged out.')
        return redirect('home')
