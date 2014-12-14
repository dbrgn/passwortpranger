# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from collections import defaultdict, namedtuple

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils.functional import cached_property


Rating = namedtuple('Rating', 'positive negative total')


class User(AbstractUser):
    """
    A custom user model that extends the default user.
    """
    def name(self):
        """
        Return either full user first and last name or the username, if no
        further data is found.
        """
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

    @cached_property
    def scores(self):
        """
        Return a dictionary with positive and negative scores.

        This property is cached on the model instance.

        """
        scores = defaultdict(dict)

        # Password length
        if self.pw_max_length == 0:
            scores['negative']['MAX_LEN_16'] = -1
        elif self.pw_max_length == 1:
            scores['negative']['MAX_LEN_10'] = -2
        elif self.pw_max_length == 3:
            scores['positive']['MAX_LEN_UNLIMITED'] = 1

        # Alphabet
        if self.alphabet_limited:
            scores['negative']['ALPHABET_LIMITED'] = -1

        # Plaintext
        if self.eml_registration_plaintext:
            scores['negative']['PW_IN_REGISTRATION_MAIL'] = -1
        if self.eml_recovery_plaintext:
            scores['negative']['NEW_PW_IN_REMEMBER_MAIL'] = -1
        if self.eml_reminder_plaintext:
            scores['negative']['OWN_PW_IN_REMEMBER_MAIL'] = -3

        # Encryption
        if self.tls == 0:
            scores['negative']['TLS_NO'] = -2
        elif self.tls == 1:
            scores['negative']['TLS_SOME'] = -1
        elif self.tls == 2:
            scores['hint']['TLS_ALL'] = 0
        elif self.tls == 3:
            scores['positive']['TLS_FORCED'] = 1

        # MFA
        if self.two_factor:
            scores['positive']['TWO_FACTOR'] = 3

        # Other
        if self.pw_strength_indicator:
            scores['positive']['SECURITY_WIDGET'] = 1

        return scores

    @cached_property
    def ratings(self):
        """
        Return namedtuple with ratings for this site.

        The namedtuple has three keys: ``positive``, ``negative``
        and ``total``.

        This property is cached on the model instance.

        """
        scores = self.scores
        sum_pos = 4 + sum(scores['positive'].itervalues())
        if sum_pos > 6:
            sum_pos = 6
        sum_neg = sum(scores['negative'].itervalues())
        if sum_neg < -6:
            sum_neg = -6
        total = sum_neg + sum_pos
        if total < 0:
            total = 0
        return Rating(sum_pos, sum_neg, total)

    def get_canonical_slug(self):
        """
        Canonical slug for the URL.
        """
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
    url = models.URLField(help_text='The URL of the website')
    email = models.EmailField(null=True, blank=True, help_text='Your e-mail address')
    comment = models.TextField(null=True, blank=True, help_text='Any comments')

    # Workflow
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='new')
    submit_date = models.DateTimeField('Submit date', auto_now_add=True)

    def __unicode__(self):
        return self.url
