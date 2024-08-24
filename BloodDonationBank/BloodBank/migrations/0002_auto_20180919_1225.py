# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='Age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='donor',
            name='PhoneNo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Hos_PhoneNo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='quantity',
            name='Hospital_Code',
            field=models.IntegerField(),
        ),
    ]
