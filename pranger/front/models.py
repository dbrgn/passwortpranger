# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """A custom user model that extends the default user."""

    def name(self):
        """Return either full user first and last name or the username, if no
        further data is found."""
        if self.first_name or self.last_name:
            return ' '.join(filter(None, [self.first_name, self.last_name]))
        return self.username


# Create your models here.
