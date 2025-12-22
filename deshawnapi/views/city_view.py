from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from deshawnapi.models import City
from rest_framework import serializers

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']

class CityView(ViewSet):
    def list(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            city = City.objects.get(pk=pk)
            serializer = CitySerializer(city)
            return Response(serializer.data)
        except City.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
