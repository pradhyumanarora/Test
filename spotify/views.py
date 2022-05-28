from django.shortcuts import redirect, render
from .credentials import REDIRECT_URI, CLIENT_ID, CLIENT_SECRET
from rest_framework.views import APIView
from requests import Request, post, get
from rest_framework import status
from rest_framework.response import Response
from .util import *
from django.shortcuts import render, redirect
from django.conf import settings
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_csrf_token(request):
    response = Response({"message": "Set CSRF cookie"})
    response["X-CSRFToken"] = get_token(request)
    return response


class AuthURL(APIView):
    def get(self,request,format = None): 
        
        scope =  "ugc-image-upload user-modify-playback-state user-read-recently-played user-read-playback-position playlist-read-collaborative user-read-playback-state user-top-read user-library-read user-read-currently-playing user-read-private user-read-email user-read-currently-playing"
        url = Request('GET',"https://accounts.spotify.com/authorize",params = {
            "client_id": CLIENT_ID,
            "response_type": "code",
            "redirect_uri": REDIRECT_URI,
            "scope": scope
        }).prepare().url

        return Response({"url":url},status = status.HTTP_200_OK)


def spotify_callback(request,format = None):
    code = request.GET.get('code')
    error = request.GET.get('error')

    response = post("https://accounts.spotify.com/api/token",data = {
        "grant_type": "authorization_code",
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')

    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_user_tokens(request.session.session_key, access_token, token_type, expires_in, refresh_token)

    return redirect('http://localhost:3000/homepage')

class IsAuthenticated(APIView):
    def get(self, request, format=None): 
        print("Auth Wala hai",self.request.session.session_key)
        session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME)
        print(session_key)   
        is_authenticated = is_spotify_authenticated(
            self.request.session.session_key)    

        return Response({'status': is_authenticated,'session_id' : self.request.session.session_key}, status=status.HTTP_200_OK)
            
# self.request.GET.get("sessionid")

class ShowData(APIView):
    def get(self,request,format = None):
        endpoint = "me"
        response_me = execute_spotify_api_request(self.request.session.session_key, endpoint)
        # headers = {'Content-Type': 'application/json','Authorization':"Bearer "+access_token}
        # # https://api.spotify.com/v1/me/top/type
        # response_me = get('https://api.spotify.com/v1/me', headers = headers)
        # response_me = response_me.json()
        # print(response_me)

        return Response(response_me,status = status.HTTP_200_OK)

class CurrentSong(APIView):
    def get(self, request, format=None):
        endpoint = "me/player/currently-playing"
        response = execute_spotify_api_request(self.request.session.session_key, endpoint)

        if 'error' in response or 'item' not in response:
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        item = response.get('item')
        duration = item.get('duration_ms')
        progress = response.get('progress_ms')
        album_cover = item.get('album').get('images')[0].get('url')
        is_playing = response.get('is_playing')
        song_id = item.get('id')

        artist_string = ""

        for i, artist in enumerate(item.get('artists')):
            if i > 0:
                artist_string += ", "
            name = artist.get('name')
            artist_string += name

        song = {
            'title': item.get('name'),
            'artist': artist_string,
            'duration': duration,
            'time': progress,
            'image_url': album_cover,
            'is_playing': is_playing,
            'votes': 0,
            'id': song_id
        }

        return Response(song, status=status.HTTP_200_OK)

# Create your views here.

# recommendations/available-genre-seeds
# me/top/artists
class Testing(APIView):
    abc = True
    Response({'status': abc}, status=status.HTTP_200_OK)