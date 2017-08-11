# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=1000)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('is_included_in_my_talent', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('number_of_likes', models.IntegerField(default=0)),
                ('number_of_upvotes', models.IntegerField(default=0)),
                ('number_of_downvotes', models.IntegerField(default=0)),
                ('view_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(to='content_management.ContentType'),
        ),
        migrations.AddField(
            model_name='content',
            name='theme',
            field=models.ForeignKey(to='content_management.Theme'),
        ),
        migrations.AddField(
            model_name='content',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
