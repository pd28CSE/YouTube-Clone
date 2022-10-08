# Generated by Django 4.1.1 on 2022-09-29 20:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channelanalytics', '0004_channel_maincontent_alter_channel_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='maincontent',
            field=models.FileField(blank=True, null=True, upload_to='mediafilles/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]