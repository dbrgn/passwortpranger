# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class User(AbstractUser):
    """A custom user model that extends the default user."""

    def name(self):
        """Return either full user first and last name or the username, if no
        further data is found."""
        if self.first_name or self.last_name:
            return ' '.join(filter(None, [self.first_name, self.last_name]))
        return self.username


class Website(models.Model):
    TLS_CHOICES = (
        (0, 'Nein'),
        (1, 'Nur Login'),
        (2, 'Überall'),
    )

    # Basic properties
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    description = models.TextField(blank=True)

    # Password
    pw_plaintext = models.NullBooleanField()
    pw_min_length = models.SmallIntegerField(null=True, blank=True)
    pw_max_length = models.SmallIntegerField(null=True, blank=True)
    pw_alphabet_size = models.SmallIntegerField(null=True, blank=True)
    pw_salted = models.NullBooleanField()
    pw_hashfunction = models.CharField(max_length=32, null=True, blank=True)

    # Other security measures
    tls = models.SmallIntegerField(choices=TLS_CHOICES)
    twofactor = models.NullBooleanField()

    def get_canonical_slug(self):
        """Canonical slug for the URL."""
        return slugify(self.name)

    def __unicode__(self):
        return self.name
