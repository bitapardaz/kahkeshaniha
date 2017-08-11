# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentViewLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.ForeignKey(to='content_management.Content')),
            ],
        ),
    ]
