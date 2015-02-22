# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_key', models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbb\xd1\x8e\xd1\x87')),
                ('products', models.CharField(max_length=200, verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd1\x8b')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
