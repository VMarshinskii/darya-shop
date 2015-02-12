# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20150205_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='home_status',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9d\xd0\xb0 \xd0\xb3\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9'),
            preserve_default=True,
        ),
    ]
