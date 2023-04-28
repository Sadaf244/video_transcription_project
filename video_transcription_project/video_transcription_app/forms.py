from django import forms
from .models import Video
class video_form(forms.ModelForm):
    class Meta:
        model=Video
        fields=['video_file']
    