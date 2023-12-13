# Generated by Django 4.2.3 on 2023-07-30 07:45

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [

        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                 primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                 primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('cover_image', models.ImageField(upload_to='covers/')),
                ('author', models.CharField(max_length=20)),
                ('availability', models.IntegerField(default=0)),
                ('edition', models.CharField(max_length=50)),
                ('isbn_issn', models.CharField(max_length=50)),
                ('series_title', models.CharField(max_length=100)),
                ('call_number', models.CharField(max_length=20)),
                ('categories', models.ManyToManyField(to='sampleApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                 help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True,
                 max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True,
                 max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True,
                 max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False,
                 help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(
                    default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(
                    default='default_username', max_length=150, unique=True)),
                ('cart_books', models.ManyToManyField(blank=True, default=list,
                 to='sampleApp.books', verbose_name='cart books')),
                ('groups', models.ManyToManyField(
                    blank=True, related_name='custom_user_set', to='auth.group', verbose_name='user groups')),
                ('user_permissions', models.ManyToManyField(
                    blank=True, related_name='custom_user_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]