from django.urls import path
from . import views
urlpatterns = [
    path('api/', views.list_movies, name='movie-list'),
]