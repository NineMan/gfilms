from rest_framework import serializers
from .models import Film


class FilmSerializer(serializers.Serializer):
    # id = serializers.CharField()
    # title = serializers.CharField()
    rusname = serializers.CharField()

class GhibliSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    rusname = serializers.CharField()
