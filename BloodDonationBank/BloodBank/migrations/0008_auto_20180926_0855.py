# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0007_auto_20180926_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='Blood_Grp',
            field=models.CharField(default='A+', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='Hos_Address',
            field=models.CharField(default='wagholi', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='Hos_Email',
            field=models.EmailField(default='g@gmail.com', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='Hos_Name',
            field=models.CharField(default='qqq', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='Hos_PhoneNo',
            field=models.IntegerField(default=4342),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='Hospital_Code',
            field=models.IntegerField(default=4334),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='stock',
            field=models.IntegerField(default=90),
            preserve_default=False,
        ),
    ]
