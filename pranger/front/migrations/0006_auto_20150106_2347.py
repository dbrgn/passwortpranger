# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_auto_20141209_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='pw_max_length',
            field=models.SmallIntegerField(choices=[(0, '<16'), (1, '<10'), (2, 'unlimited')]),
            preserve_default=True,
        ),
    ]
