# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count_status',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='related_products',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_status',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xa1\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0\xd1\x82\xd1\x8c \xd1\x81\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd1\x83'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xba\xd0\xbb\xd0\xb0\xd0\xbc\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xbc\xd0\xb5\xd1\x82\xd0\xba\xd0\xb8'),
            preserve_default=True,
        ),
    ]
