# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-06-03 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_profile_profile_pix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(max_length=50),
        ),
    ]
