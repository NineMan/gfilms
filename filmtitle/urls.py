from django.urls import path
# from .views import FilmView, GhibliFilmView
from .views import GhibliFilmView


app_name = 'filmtitle'

urlpatterns = [
    path('film/<uuid:uuid>', GhibliFilmView.as_view()),
    # path('film/<str>', FilmView.as_view()),
]
