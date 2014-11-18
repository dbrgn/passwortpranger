# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='alphabet_limited',
            field=models.NullBooleanField(help_text='Is the password alphabet limited?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='website',
            name='securitywidget',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='website',
            name='twofactor',
            field=models.NullBooleanField(help_text='Does the website offer some kind of 2 factor authentication?'),
            preserve_default=True,
        ),
    ]
