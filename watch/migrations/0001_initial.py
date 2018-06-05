# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-04 21:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bussiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bussiness_name', models.CharField(max_length=30)),
                ('Email_adress', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('location', models.CharField(max_length=30)),
                ('occupant_count', models.PositiveIntegerField(default=0)),
                ('hood_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('comment', models.TextField()),
                ('user_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('police_station', models.CharField(blank=True, max_length=30, null=True)),
                ('police_no', models.IntegerField(default=0)),
                ('police_address', models.CharField(blank=True, max_length=30, null=True)),
                ('healthcare_centre', models.CharField(blank=True, max_length=30, null=True)),
                ('healthcare_no', models.IntegerField()),
                ('healthcare_address', models.CharField(blank=True, max_length=20, null=True)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='User_prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_confirm', models.BooleanField(default=False)),
                ('phone_num', models.IntegerField(verbose_name=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Neighborhood')),
            ],
        ),
        migrations.AddField(
            model_name='bussiness',
            name='Neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Neighborhood'),
        ),
        migrations.AddField(
            model_name='bussiness',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]