from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from deshawnapi.models import Dog
from rest_framework import serializers

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed']

class DogView(ViewSet):
    def list(self, request):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            dog = Dog.objects.get(pk=pk)
            serializer = DogSerializer(dog)
            return Response(serializer.data)
        except Dog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
