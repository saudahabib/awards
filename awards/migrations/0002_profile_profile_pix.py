# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-06-03 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pix',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
