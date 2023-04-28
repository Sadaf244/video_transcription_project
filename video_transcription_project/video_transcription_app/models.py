from django.db import models
class Video(models.Model):
    video_url=models.CharField(max_length=100,null=True, blank=True)
    video_file = models.FileField(null=True, blank=True)
    transcript=models.CharField(max_length=200,null=True, blank=True)
    