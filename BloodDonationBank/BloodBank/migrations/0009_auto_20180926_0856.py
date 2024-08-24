# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0008_auto_20180926_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='id',
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Hospital_Code',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
