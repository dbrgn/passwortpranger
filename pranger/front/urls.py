# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from django.conf.urls import patterns, url

from front import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^info/$', views.InfoView.as_view(), name='info'),
    url(r'^website/(?P<slug>[\w-]+)-(?P<pk>\d+)/$', views.WebsiteView.as_view(), name='website'),
    url(r'^submit/$', views.SubmissionView.as_view(), name='submission'),
    url(r'^submit/thanks/$', views.SubmissionThanksView.as_view(), name='submission_thanks'),
)
