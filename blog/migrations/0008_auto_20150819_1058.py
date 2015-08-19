# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150819_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pub_date',
            new_name='pubdate',
        ),
    ]
