# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0004_auto_20180919_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='Hospital_Code_do',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='Patient_Id_Hos',
        ),
        migrations.RemoveField(
            model_name='quantity',
            name='Hospital_Code_qty',
        ),
        migrations.AddField(
            model_name='hospital',
            name='Blood_Grp',
            field=models.CharField(default='A+', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='stock',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Quantity',
        ),
    ]
