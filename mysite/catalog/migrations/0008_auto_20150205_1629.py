# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20150205_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='step',
            field=models.IntegerField(verbose_name=b'\xd0\x92\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c', blank=True),
            preserve_default=True,
        ),
    ]
