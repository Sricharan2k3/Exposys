# Generated by Django 4.2.2 on 2023-07-31 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleApp', '0008_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]