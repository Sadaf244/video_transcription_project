from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("video_transcription_app/", include("video_transcription_app.urls")),   
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)