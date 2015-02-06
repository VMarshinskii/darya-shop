# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20150205_1824'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([]),
        ),
    ]
