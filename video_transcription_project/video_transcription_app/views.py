from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import video_form
from .models import Video
from django.views.generic.edit  import CreateView
from django.views.generic import ListView
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Video
import os
import moviepy.editor as mp
from django.core.files.storage import FileSystemStorage
from moviepy.editor import VideoFileClip
import speech_recognition as sr
# from rest_framework.response import Response
class AcceptVideoURL(View):
    def get(self, request):
        form=video_form()
        return render(request, "transcribe_video.html"
        ,{"form":form
        })
    def post(self, request,id=None):
        form = video_form(request.POST, request.FILES)
        if form.is_valid():
            video_file = form.cleaned_data['video_file']
            path = os.path.join(settings.MEDIA_ROOT, video_file.name)
            with open(path, 'wb+') as destination:
                for chunk in video_file.chunks():
                    destination.write(chunk)

            # Create a new Video object and save it to the database
            video = form.save(commit=False)
            video.video_url = path
            video.save()

            # Load the video file as a clip
            video_storage = FileSystemStorage()
            video_path = video_storage.path(video_file.name)
            video_clip = VideoFileClip(video_path)

            # Extract the audio from the clip and save it as a WAV file
            audio_clip = video_clip.audio
            audio_filename = f"{video_file.name.split('.')[0]}.wav"
            audio_path = video_storage.path(audio_filename)
            audio_clip.write_audiofile(audio_path)

            # Transcribe the audio using Google Cloud Speech-to-Text
            r = sr.Recognizer()
            with sr.AudioFile(audio_path) as source:
                audio_data = r.record(source)
            text = r.recognize_google(audio_data)
            context = {
                'result': text,
            }

            # Delete the audio file
            video_storage.delete(audio_filename)
            video=Video(video_url = path)
            video.save()
            # Return the transcription result
            return render(request, "video_transcription_app/transcription_result.html", context)
        else:
            form = VideoForm()
       