from django.contrib import admin
from .models import *
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display=('id','video_url','video_file')
admin.site.register(Video,VideoAdmin)