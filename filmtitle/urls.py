from django.urls import path
from .views import GhibliFilmView


app_name = 'filmtitle'

urlpatterns = [
    path('film/<uuid:uuid>', GhibliFilmView.as_view()),
]
