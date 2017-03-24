# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac_address', models.CharField(unique=True, max_length=50)),
                ('hostname', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50, unique=True, null=True)),
                ('last_seen', models.DateTimeField(null=True)),
                ('location', models.CharField(max_length=100, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
