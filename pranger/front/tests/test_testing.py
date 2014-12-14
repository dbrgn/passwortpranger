# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import pytest

from django.contrib.auth import get_user_model


def test_dummy():
    """
    Assert that 1 + 1 equals 2.
    """
    one = 1
    assert one + 1 == 2


@pytest.mark.django_db
def test_database():
    """
    Check whether database access works.
    """
    User = get_user_model()
    assert User.objects.count() == 0
    User.objects.create(username='dummy', email='dummy@example.com')
    assert User.objects.count() == 1
