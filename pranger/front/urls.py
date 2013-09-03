# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from django.conf.urls import patterns, include, url

from front import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^auth/login/$', views.LoginView.as_view(), name='login'),
    url(r'^auth/login-successful/$', views.LoginSuccessfulView.as_view(), name='login-successful'),
    url(r'^auth/logout/$', views.LogoutView.as_view(), name='logout'),
)
