# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0009_auto_20180926_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=999, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Hospital_Code',
            field=models.IntegerField(),
        ),
    ]
