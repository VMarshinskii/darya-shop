# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('description', models.CharField(max_length=200, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('keyword', models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xb2\xd1\x8b\xd0\xb5 \xd1\x81\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xb0')),
                ('text', redactor.fields.RedactorField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82')),
                ('url', models.CharField(max_length=200, verbose_name=b'Url')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('description', models.CharField(max_length=200, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('keyword', models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xb2\xd1\x8b\xd0\xb5 \xd1\x81\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xb0')),
                ('text', redactor.fields.RedactorField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82')),
                ('url', models.CharField(max_length=200, verbose_name=b'Url')),
            ],
            options={
                'verbose_name': '\u0420\u0430\u0437\u0434\u0435\u043b',
                'verbose_name_plural': '\u0420\u0430\u0437\u0434\u0435\u043b\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='page',
            name='section',
            field=models.ForeignKey(default=b'-1', blank=True, to='pages.Section', help_text=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xb4\xd0\xb5\xd0\xbb', null=True),
            preserve_default=True,
        ),
    ]
