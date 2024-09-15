from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Movies
from . serializers import MoviesSerializer
from rest_framework import status

# Create your views here.

# class based API view
class MoviesView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                movie = Movies.objects.get(id=id)
                serializer = MoviesSerializer(movie, many=False)
                return Response({'message': 'list_movies: this is api GET view', 'data': serializer.data})
            except Movies.DoesNotExist:
                return Response ({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            all_movies = Movies.objects.all()
            serializer = MoviesSerializer(all_movies, many=True)
            return Response({'message': 'list_movies: this is api GET view', 'data': serializer.data})

    def post(self, request):
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'list_movies: this is api POST view', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            movie = Movies.objects.get(id=id)
        except Movies.DoesNotExist:
            return Response ({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MoviesSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Movie updated successfully', 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            movie = Movies.objects.get(id=id)
        except Movies.DoesNotExist:
            return Response ({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MoviesSerializer(movie, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Movie updated successfully', 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            movie = Movies.objects.get(id=id)
        except Movies.DoesNotExist:
            return Response({'message': 'movie not found'}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# function based API view
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def list_movies(request):
    if request.method == 'GET':
        return Response({'message': 'list_movies: this is api GET view'})
    if request.method == 'POST':
        return Response({'message': 'list_movies: this is api POST view'})
    if request.method == 'PUT':
        return Response({'message': 'list_movies: this is api PUT view'})
    if request.method == 'PATCH':
        return Response({'message': 'list_movies: this is api PATCH view'})
    if request.method == 'DELETE':
        return Response({'message': 'list_movies: this is api DELETE view'})



