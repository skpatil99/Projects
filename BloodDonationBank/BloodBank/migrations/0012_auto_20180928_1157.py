# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodBank', '0011_auto_20180926_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('Hos_Code', models.IntegerField(serialize=False, primary_key=True, db_index=True)),
                ('User_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Blood_Grp',
            field=models.CharField(max_length=10, db_index=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Hospital_Code',
            field=models.IntegerField(db_index=True),
        ),
    ]
