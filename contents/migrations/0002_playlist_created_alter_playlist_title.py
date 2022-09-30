# Generated by Django 4.1.1 on 2022-09-30 16:42

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='playlist',
            name='title',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Play List Name'),
        ),
    ]
