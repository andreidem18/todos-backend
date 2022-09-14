from django.shortcuts import render

from config.get_client_ip import get_client_ip
from .models import Todo
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'isCompleted')

class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'isCompleted', 'created_by')

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(created_by=get_client_ip(request))
        serialized = TodoSerializer(queryset, many=True)
        return Response(serialized.data)

    
    def create(self, request, *args, **kwargs):
        request.data['created_by']=get_client_ip(request)
        serialized = CreateTodoSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(status = status.HTTP_400_BAD_REQUEST, data = serialized.errors)
        else:
            serialized.save()
            serialized = TodoSerializer(serialized.data)
            return Response(status = status.HTTP_201_CREATED, data = serialized.data)
