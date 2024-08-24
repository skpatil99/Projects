# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0010_auto_20180926_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='Patient_Id',
        ),
        migrations.AddField(
            model_name='donor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=99, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
