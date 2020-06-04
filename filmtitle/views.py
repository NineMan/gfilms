import requests
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Film
from .serializer import GhibliSerializer


class GhibliFilmView(APIView):

    def get(self, request, uuid):
        URL = 'https://ghibliapi.herokuapp.com/films/'
        url = URL + str(uuid)
        response = requests.get(url)
        data = json.loads(response.text)
        film = Film.objects.filter(uuid=uuid)
        if film.exists():
            rusname = film[0].rusname
        else:
            rusname = None
        data['rusname'] = rusname
        ghibliserializer = GhibliSerializer(data=data)
        ghibliserializer.is_valid()
        return Response(ghibliserializer.data)


