from django.urls import path

from . import views

urlpatterns = [
    path("", views.AcceptVideoURL.as_view()),
   
]