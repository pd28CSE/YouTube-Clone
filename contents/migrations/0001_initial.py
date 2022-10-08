# Generated by Django 4.1.1 on 2022-09-30 16:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channelanalytics', '0006_alter_channel_maincontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5)])),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlist', to='channelanalytics.channel', verbose_name='Channel Name')),
            ],
        ),
    ]