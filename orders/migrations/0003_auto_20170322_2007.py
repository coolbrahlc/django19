# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 18:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20170322_2005'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProdInOrder',
            new_name='ProductInOrder',
        ),
    ]