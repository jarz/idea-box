# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 23:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='voters',
            field=models.ManyToManyField(related_name='idea_vote_creator', through='idea.Vote', to=settings.AUTH_USER_MODEL),
        ),
    ]
