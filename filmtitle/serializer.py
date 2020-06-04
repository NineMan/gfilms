from rest_framework import serializers


class GhibliSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    rusname = serializers.CharField()
    description = serializers.CharField()
    director = serializers.CharField()
    release_date = serializers.CharField()
    producer = serializers.CharField()
    rt_score = serializers.CharField()
    people = serializers.CharField()
    species = serializers.CharField()
    locations = serializers.CharField()
    vehicles = serializers.CharField()
    url = serializers.CharField()
