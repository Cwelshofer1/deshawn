from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from deshawnapi.models import Walker
from rest_framework import serializers

class WalkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walker
        fields = ['id', 'name', 'email', 'city']

class WalkerView(ViewSet):
    def list(self, request):
        walkers = Walker.objects.all()
        serializer = WalkerSerializer(walkers, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            walker = Walker.objects.get(pk=pk)
            serializer = WalkerSerializer(walker)
            return Response(serializer.data)
        except Walker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
