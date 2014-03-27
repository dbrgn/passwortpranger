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
        (3, 'Forced')
    )
    PW_MAX_LENGTH_CHOICES = (
        (0, '< 16'),
        (1, '<10'),
        (2, 'unlimited')
    )
    # Basic properties
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    description = models.TextField(blank=True)

    # Password
    pw_max_length = models.SmallIntegerField(choices=PW_MAX_LENGTH_CHOICES)
    pw_alphabet_size_restricted = models.BooleanField()

    #delivery
    remember_mail_has_own_password = models.BooleanField()
    remember_mail_has_new_password = models.BooleanField()
    new_user_mail_has_own_password = models.BooleanField()

    # Email
    eml_reg_plaintext = models.NullBooleanField(
            help_text='Does the registration email contain the password in plaintext?')
    eml_remind_plaintext = models.NullBooleanField(
            help_text='Does the password remainder email contain the password in plaintext?')

    # Other security measures
    tls = models.SmallIntegerField(choices=TLS_CHOICES)
    twofactor = models.NullBooleanField()
    securitywidget = models.BooleanField()
    def get_canonical_slug(self):
        """Canonical slug for the URL."""
        return slugify(self.name)

    def __unicode__(self):
        return self.name


class Bewertung():
    BASE_POINTS = 3
    PW_MAX_LENGTH = (
        (0, -1),
        (1, -2),
        (2, 1)
    )
    ALPHABET_SIZE_RESTRICTED = -1
    NEW_PASSWORD_IN_REMBMER_MAIL = -1
    OWN_PASSWORD_IN_REMBMER_MAIL = -3
    OWN_PASSWORD_IN_REGISTER_MAIL = -1
    TLS_SCORE = (
        (0, -2),
        (1, -1),
        (2, 0),
        (3, 1)
    )
    TWO_FACTOR = 3
    SECURITY_WIDGET = 1

    actual_points = 0
    def __init__(self, website):
        self.actual_points = self.BASE_POINTS + self.PW_MAX_LENGTH[website.pw_max_length]
