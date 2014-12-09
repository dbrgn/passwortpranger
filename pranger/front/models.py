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
        (1, 'Partiell'),
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
    alphabet_limited = models.NullBooleanField(
        help_text='Is the password alphabet limited?')

    # Email
    eml_registration_plaintext = models.NullBooleanField(
        help_text='Does the registration email contain the password in plaintext?')
    eml_reminder_plaintext = models.NullBooleanField(
        help_text='Does the password reminder email contain the user password in plaintext?')
    eml_recovery_plaintext = models.NullBooleanField(
        help_text='Does the password recovery email contain a temporary password in plaintext?')

    # Other security measures
    tls = models.SmallIntegerField(choices=TLS_CHOICES)
    two_factor = models.NullBooleanField(
        help_text='Does the website offer some kind of 2 factor authentication?')
    pw_strength_indicator = models.NullBooleanField(
        help_text='Does the website offer a visual password strength indicator?')

    def get_canonical_slug(self):
        """Canonical slug for the URL."""
        return slugify(self.name)

    def __unicode__(self):
        return self.name


class Submission(models.Model):
    """
    A website submission by a user.
    """
    STATUS_CHOICES = (
        ('new', 'New'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    # Submission data
    url = models.URLField(
        help_text='The URL of the website')
    email = models.EmailField(null=True, blank=True,
        help_text='Your e-mail address')
    comments = models.TextField(null=True, blank=True,
        help_text='Any comments')

    # Workflow
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
