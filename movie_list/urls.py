from django.urls import path
from . import views
urlpatterns = [
    path('api/', views.list_movies, name='movie-list'),
    path('classApi/', views.MoviesView.as_view(), name='movies'),
    path('classApi/<int:id>/', views.MoviesView.as_view(), name='movies'),
]