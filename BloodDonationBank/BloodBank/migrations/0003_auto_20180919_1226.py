# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0002_auto_20180919_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
