# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('openwisp_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
