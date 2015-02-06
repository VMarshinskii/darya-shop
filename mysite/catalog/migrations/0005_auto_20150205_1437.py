# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20150204_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=200, verbose_name=b'Description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='keywords',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xb2\xd1\x8b\xd0\xb5 \xd1\x81\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xb0', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='step',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x92\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.CharField(max_length=200, verbose_name=b'Url', blank=True),
            preserve_default=True,
        ),
    ]
