# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-19 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=1000)),
                ('product_weight', models.IntegerField(default=1000)),
                ('product_category', models.CharField(max_length=50)),
                ('product_cost', models.IntegerField(default=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]
