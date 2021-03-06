# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 08:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('need', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CategoryDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('need', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('need', models.IntegerField()),
                ('select', models.BooleanField()),
                ('category_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check.CategoryDetail')),
            ],
        ),
    ]
