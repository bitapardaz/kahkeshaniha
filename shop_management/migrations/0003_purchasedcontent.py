# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0002_content_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop_management', '0002_auto_20170811_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasedContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('rrn', models.CharField(max_length=100)),
                ('content', models.ForeignKey(to='content_management.Content')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
