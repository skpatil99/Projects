# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('Patient_Id', models.IntegerField(serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=64)),
                ('Age', models.IntegerField(max_length=4)),
                ('Gender', models.CharField(max_length=10)),
                ('Blood_Grp', models.CharField(max_length=10)),
                ('PhoneNo', models.IntegerField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('Hospital_Code', models.IntegerField(serialize=False, primary_key=True)),
                ('Hos_Name', models.CharField(max_length=64)),
                ('Hos_Address', models.CharField(max_length=64)),
                ('Hos_PhoneNo', models.IntegerField(max_length=12)),
                ('Hos_Email', models.EmailField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Hospital_Code_do', models.ForeignKey(to='BloodBank.Hospital')),
                ('Patient_Id_Hos', models.ForeignKey(to='BloodBank.Donor')),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Blood_Grp', models.CharField(max_length=10)),
                ('Hospital_Code', models.IntegerField(max_length=40)),
                ('stock', models.IntegerField(max_length=100)),
            ],
        ),
    ]
