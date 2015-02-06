# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('price', models.IntegerField(verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0')),
                ('sale', models.IntegerField(verbose_name=b'\xd0\xa1\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xb0, %')),
                ('sale_status', models.IntegerField(verbose_name=b'\xd0\xa1\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0\xd1\x82\xd1\x8c \xd1\x81\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd1\x83')),
                ('count', models.IntegerField(verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80 \xd0\xb2 \xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb8\xd0\xb8')),
                ('status', models.IntegerField(verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xba\xd0\xbb\xd0\xb0\xd0\xbc\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xbc\xd0\xb5\xd1\x82\xd0\xba\xd0\xb8')),
                ('text', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('keywords', models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xb2\xd1\x8b\xd0\xb5 \xd1\x81\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xb0')),
                ('description', models.CharField(max_length=200, verbose_name=b'Description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
