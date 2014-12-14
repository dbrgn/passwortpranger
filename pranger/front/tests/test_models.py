# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import pytest

from front import models


@pytest.mark.parametrize(['properties', 'pos', 'neg', 'sum_pos', 'sum_neg', 'sum_total'], [
    # Perfect score (only positive, no negative)
    ({
        'pw_max_length': models.Website.PW_MAX_LENGTH_CHOICES.unlimited,
        'alphabet_limited': False,
        'eml_registration_plaintext': False,
        'eml_reminder_plaintext': False,
        'eml_recovery_plaintext': False,
        'tls': models.Website.TLS_CHOICES.forced,
        'two_factor': True,
        'pw_strength_indicator': True,
    }, 6, 0, 6, 0, 6),
    # Worst possible score (only negative, no positive)
    ({
        'pw_max_length': models.Website.PW_MAX_LENGTH_CHOICES.below_10,
        'alphabet_limited': True,
        'eml_registration_plaintext': True,
        'eml_reminder_plaintext': True,
        'eml_recovery_plaintext': True,
        'tls': models.Website.TLS_CHOICES.no,
        'two_factor': False,
        'pw_strength_indicator': False,
    }, 0, -10, 4, -6, 0),
    # Worst possible score (only negative, no positive)
    ({
        'pw_max_length': models.Website.PW_MAX_LENGTH_CHOICES.unlimited,
        'alphabet_limited': False,
        'eml_registration_plaintext': False,
        'eml_reminder_plaintext': False,
        'eml_recovery_plaintext': False,
        'tls': models.Website.TLS_CHOICES.everywhere,
        'two_factor': False,
        'pw_strength_indicator': False,
    }, 1, 0, 5, 0, 5),
])
def test_website_rating(properties, pos, neg, sum_pos, sum_neg, sum_total):
    """
    Assert that the ratings are calculated correctly.
    """
    site = models.Website(**properties)

    scores = site.scores
    assert pos == sum(scores['positive'].itervalues())
    assert neg == sum(scores['negative'].itervalues())

    ratings = site.ratings
    assert sum_pos == ratings.positive
    assert sum_neg == ratings.negative
    assert sum_total == ratings.total
