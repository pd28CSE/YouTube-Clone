# Generated by Django 4.1.1 on 2022-09-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_alter_videocontent_react'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocontent',
            name='react',
            field=models.ManyToManyField(blank=True, related_name='content', to='contents.userreact', verbose_name='User Reaction'),
        ),
    ]
