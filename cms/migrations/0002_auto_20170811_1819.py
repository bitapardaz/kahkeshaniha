# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalentBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_link', models.CharField(max_length=1000)),
                ('order', models.IntegerField(default=100)),
                ('content_type', models.ForeignKey(to='cms.ContentType')),
            ],
        ),
        migrations.RemoveField(
            model_name='talent_banner',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='Talent_banner',
        ),
    ]
