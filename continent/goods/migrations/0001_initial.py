# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-03 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_auto_20160903_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Краткое описание')),
                ('content', models.TextField(verbose_name='Полное описание')),
                ('price', models.FloatField(db_index=True, verbose_name='Цена, руб.')),
                ('price_acc', models.FloatField(blank=True, null=True, verbose_name='Цена с учетом скидки, руб.')),
                ('in_stock', models.BooleanField(db_index=True, default=True, verbose_name='Есть в наличии')),
                ('is_new', models.BooleanField(db_index=True, default=False, verbose_name='Новый')),
                ('image', models.ImageField(upload_to='goods/list', verbose_name='Основное изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Subcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
        migrations.CreateModel(
            name='GoodImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='goods/detail', verbose_name='Дополнительное изображение')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Good')),
            ],
            options={
                'verbose_name': 'изображение к товару',
                'verbose_name_plural': 'изображения к товару',
            },
        ),
    ]