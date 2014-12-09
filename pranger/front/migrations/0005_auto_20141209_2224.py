# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_submission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='comments',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='submission',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 9, 21, 57, 52, 114109, tzinfo=utc), verbose_name='Submit date', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(default='new', max_length=16, choices=[('new', 'New'), ('accepted', 'Accepted'), ('rejected', 'Rejected')]),
            preserve_default=True,
        ),

    ]
