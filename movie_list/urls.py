from django.urls import path
from . import views
urlpatterns = [
    path('api/', views.list_movies, name='movie-list'),
    path('classApi/', views.Movies.as_view(), name='movies'),

]