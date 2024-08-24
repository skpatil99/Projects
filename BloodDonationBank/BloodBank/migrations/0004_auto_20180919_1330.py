# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0003_auto_20180919_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quantity',
            name='Hospital_Code',
        ),
        migrations.AddField(
            model_name='quantity',
            name='Hospital_Code_qty',
            field=models.ForeignKey(default=999, to='BloodBank.Hospital'),
        ),
    ]
