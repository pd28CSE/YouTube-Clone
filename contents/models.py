from django.db import models
from django.core.validators import MinLengthValidator, FileExtensionValidator

from user.models import User
from channelanalytics.models import Channel

# Create your models here.

class PlayList(models.Model):
    
    title = models.CharField(blank=False, verbose_name='Play List Name', max_length=50,
        validators=[MinLengthValidator(5)])
    channel = models.ForeignKey(Channel, verbose_name='Channel Name', 
        on_delete=models.CASCADE, related_name='playlist')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title.title() + f'   ||   {self.channel}   ||   {self.channel.user}'
    
    class Meta:
        unique_together = ['title', 'channel']
        verbose_name_plural = 'Play List'


class VideoContent(models.Model):

    contenttitle = models.CharField(max_length=300, blank=False)
    playlisttitle = models.ForeignKey(PlayList, verbose_name='Select Play List Name', 
        on_delete=models.CASCADE, related_name='videocontents')
    file = models.FileField(blank=False, verbose_name='Your Video Content', 
        validators=[FileExtensionValidator(
            allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv']
        )])
    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.contenttitle.title()
    
    class Meta:
        verbose_name = 'Video Content'
        verbose_name_plural = 'Video Contents'


class UserReact(models.Model):
    
    REACT_CHOICES = [
        ('LO', 'Love'),
        ('AN', 'Angry'),
        ('LI', 'Like'),
        ('DI', 'Dislike'),
        ('NO', 'NO React')
    ]
    
    user = models.ForeignKey(User, verbose_name='Liked User', on_delete=models.CASCADE, related_name='reactuser')
    content = models.ManyToManyField(VideoContent, verbose_name='Select Content', related_name='react')
    react = models.CharField(max_length=2, choices=REACT_CHOICES)

    def __str__(self) -> bool:
        return self.react
    
    class Meta:
        verbose_name_plural = 'User React'