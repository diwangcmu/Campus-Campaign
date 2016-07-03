# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-06 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ccm', '0008_auto_20160206_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=1000)),
                ('useremail', models.CharField(default='', max_length=1000)),
                ('campaign', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ccm.Campaign')),
            ],
        ),
    ]