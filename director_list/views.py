from rest_framework import generics
from rest_framework.response import Response

from . models import Directors
from . serializers import DirectorSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class DirecotorList(generics.ListCreateAPIView):
    queryset = Directors.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAdminUser] # use AllowAny if you need

    def list(self, request):
        queryset = self.get_queryset()
        serializer = DirectorSerializer(queryset, many=True)
        return Response ({'result': serializer.data})

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)