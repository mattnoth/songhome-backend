from django.contrib import admin
from .models import Song, Comment, Writer, Tag

# Register your models here.
admin.site.register(Song)
admin.site.register(Comment)
admin.site.register(Writer)
admin.site.register(Tag)
