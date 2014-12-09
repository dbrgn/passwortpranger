# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20141118_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='website',
            old_name='eml_recover_plaintext',
            new_name='eml_recovery_plaintext',
        ),
        migrations.RenameField(
            model_name='website',
            old_name='eml_remind_plaintext',
            new_name='eml_reminder_plaintext',
        ),
        migrations.RenameField(
            model_name='website',
            old_name='twofactor',
            new_name='two_factor',
        ),
        migrations.RemoveField(
            model_name='website',
            name='securitywidget',
        ),
        migrations.AddField(
            model_name='website',
            name='pw_strength_indicator',
            field=models.NullBooleanField(help_text='Does the website offer a visual password strength indicator?'),
            preserve_default=True,
        ),
    ]
