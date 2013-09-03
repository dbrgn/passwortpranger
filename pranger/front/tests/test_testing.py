# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import pytest

from front.models import User


def test_dummy():
    """Assert that the Webrepublic is awesome."""
    webrepublic = 'awesome'
    assert webrepublic == 'awesome'


@pytest.mark.django_db
def test_database():
    """Check whether database access works."""
    assert User.objects.count() == 0
    User.objects.create(username='dummy', email='dummy@example.com')
    assert User.objects.count() == 1
