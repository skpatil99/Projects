# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0005_auto_20180921_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=99, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Hospital_Code',
            field=models.IntegerField(),
        ),
    ]
