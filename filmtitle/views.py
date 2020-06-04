import requests
import json
from rest_framework.generics import get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Film
from .serializer import FilmSerializer
from .serializer import GhibliSerializer


class FilmView(APIView):

    def get(self, request, uuid):
        # url = 'https://ghibliapi.herokuapp.com/films/ebbb6b7c-945c-41ee-a792-de0e43191bd8'
        # response = requests.get(url)
        # data = json.loads(response.text)

        film = get_object_or_404(Film.objects.filter(uuid=uuid))
        # serializer = FilmSerializer(film, data=data)
        serializer = FilmSerializer(film)
        # serializer.is_valid()
        return Response(serializer.data)


class GhibliFilmView(APIView):

    def get(self, request, uuid):
        URL = 'https://ghibliapi.herokuapp.com/films/'
        url = URL + str(uuid)
        response = requests.get(url)
        data = json.loads(response.text)
        film = Film.objects.filter(uuid=uuid)
        if film.exists():
            rusname = film.rusname
        else:
            rusname = None
        data['rusname'] = rusname
        ghibliserializer = GhibliSerializer(data=data)
        ghibliserializer.is_valid()
        return Response(ghibliserializer.data)


