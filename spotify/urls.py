from django.urls import path
from spotify.views import *

app_name = 'spotify'

urlpatterns = [
    path('auth',AuthURL.as_view()),
    path('redirect',spotify_callback),
    path('is-authenticated', IsAuthenticated.as_view()),
    path('print',ShowData.as_view()),
    path('current-song',CurrentSong.as_view()),    
    path('csrf/', get_csrf_token),
    path('testing',Testing.as_view())
]

# get-aut-url