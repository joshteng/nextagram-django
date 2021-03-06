# Generated by Django 3.0.5 on 2020-04-07 23:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
import flask_login.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('role', models.CharField(default='user', max_length=100)),
                ('profile_picture', models.TextField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'user',
            },
            bases=(flask_login.mixins.UserMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('image_path', models.TextField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj.User')),
            ],
            options={
                'db_table': 'image',
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.IntegerField(default=0)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj.User')),
            ],
            options={
                'db_table': 'donation',
            },
        ),
    ]
