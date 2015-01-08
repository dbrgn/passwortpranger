# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0006_auto_20150106_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='pw_max_length',
            field=models.SmallIntegerField(choices=[(0, '<16'), (1, '<10'), (2, 'Unlimitiert'), (3, '>=16')]),
            preserve_default=True,
        ),
    ]
