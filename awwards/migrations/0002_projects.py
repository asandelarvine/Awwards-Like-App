# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2021-12-12 06:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awwards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=255)),
                ('project_image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('project_description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('link', models.URLField()),
                ('country', django_countries.fields.CountryField(default='KE', max_length=2)),
                ('Author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('author_profile', models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='awwards.Profile')),
            ],
            options={
                'verbose_name': 'My Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['-pub_date'],
            },
        ),
    ]
