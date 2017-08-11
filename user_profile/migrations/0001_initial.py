# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInterest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theme', models.ForeignKey(to='content_management.Theme')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_number', models.CharField(max_length=20)),
                ('otp', models.IntegerField(default=0)),
                ('expiry_datetime', models.DateTimeField()),
                ('followers', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
                ('thumbnail', models.ImageField(upload_to=b'images')),
                ('is_shop_activated', models.BooleanField(default=False)),
                ('is_vote_allowance_unlimited', models.BooleanField(default=False)),
                ('vote_allowance', models.IntegerField(default=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.ForeignKey(to='user_profile.UserType'),
        ),
    ]
