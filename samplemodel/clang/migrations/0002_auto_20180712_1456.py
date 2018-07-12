# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-12 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clanguagesales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copies', models.IntegerField()),
                ('mode_sales', models.CharField(choices=[('shop', 'Visited Shop'), ('web', 'Online Sales')], max_length=6)),
                ('bookname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clang.Clanguage')),
            ],
            options={
                'db_table': 'csales',
            },
        ),
        migrations.CreateModel(
            name='Clocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=250)),
                ('pincode', models.IntegerField()),
            ],
            options={
                'db_table': 'carea',
            },
        ),
        migrations.AddField(
            model_name='clanguagesales',
            name='location',
            field=models.ManyToManyField(to='clang.Clocation'),
        ),
    ]
