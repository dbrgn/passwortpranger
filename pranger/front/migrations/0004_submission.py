# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_auto_20141209_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(help_text='The URL of the website')),
                ('email', models.EmailField(help_text='Your e-mail address', max_length=75, null=True, blank=True)),
                ('comments', models.TextField(help_text='Any comments', null=True, blank=True)),
                ('status', models.CharField(max_length=16, choices=[('new', 'New'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
