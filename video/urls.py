from django.urls import path, include
from video.views import views

urlpatterns = [
    path('',views.video_view),
]
