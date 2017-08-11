# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AlowanceItem',
            new_name='AllowanceItem',
        ),
    ]
