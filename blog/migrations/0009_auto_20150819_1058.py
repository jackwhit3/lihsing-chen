# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150819_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pubdate',
            new_name='pub_date',
        ),
    ]
