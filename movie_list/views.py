from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class Movies(APIView):
    def get(self, request):
        data = {
            "name": 'akbar ali',
            "age": 25,
            "place": 'ekd'
        }
        return Response({'message': 'list_movies: this is api GET view', 'response': data})

    def post(self, request):
        return Response({'message': 'list_movies: this is api POST view'})



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



