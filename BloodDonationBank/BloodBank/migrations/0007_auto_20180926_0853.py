# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0006_auto_20180926_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='Blood_Grp',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='Hos_Address',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='Hos_Email',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='Hos_Name',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='Hos_PhoneNo',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='Hospital_Code',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='stock',
        ),
    ]
