# Generated by Django 4.1.1 on 2022-09-30 17:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channelanalytics', '0006_alter_channel_maincontent'),
        ('contents', '0002_playlist_created_alter_playlist_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('react', models.CharField(choices=[('L', 'Love'), ('A', 'Angry'), ('L', 'Like'), ('D', 'Dislike'), ('N', 'NO React')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactuser', to=settings.AUTH_USER_MODEL, verbose_name='Liked User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='playlist',
            unique_together={('title', 'channel')},
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenttitle', models.CharField(max_length=300)),
                ('file', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])], verbose_name='Your Video Content')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('playlisttitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videocontents', to='contents.playlist', verbose_name='Select Play List Name')),
                ('react', models.ManyToManyField(related_name='content', to='contents.userreact', verbose_name='User Reaction')),
            ],
        ),
    ]