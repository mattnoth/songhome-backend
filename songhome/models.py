from django.db import models
from django.utils import timezone, dates
from datetime import datetime, date

# Create your models here.


class Song(models.Model): 
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='media/images/', default='images/default.jpg')
    file = models.FileField(upload_to='media/audio/', default='default.mp3')
    created = models.DateTimeField(auto_now_add=True)
    release_date = models.DateField(null=True, blank=True)
    isrc_code = models.IntegerField(blank=True, null=True)
    lyrics = models.CharField(blank=True, max_length=5000, null=True)
    bpm = models.SmallIntegerField(blank=True, null=True)
    status = models.CharField(blank=True, max_length=100, null=True)
    key = models.CharField(blank=True, max_length=100, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    related_position = models.IntegerField(null=True, blank=True)

    # def __str__(self):
    #     return self.slug

class Writer(models.Model):
    name = models.CharField(max_length=100)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='writers')
    pub_percent = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model): 
    name = models.CharField(max_length=100)
    song = models.ForeignKey(
        Song, on_delete=models.CASCADE, related_name='tags')
    
    def __str__(self):
        return self.name
