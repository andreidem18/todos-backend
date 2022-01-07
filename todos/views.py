from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from items.models import Item
from priorities.models import Priority
from .models import Todo
from rest_framework import serializers, viewsets

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ('id', 'priority')

class TodoSerializer(serializers.ModelSerializer):
    priority = PrioritySerializer(read_only=True)
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'deadline', 'done', 'priority')
        
class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'deadline', 'done', 'priority')


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateTodoSerializer
        return super().get_serializer_class()
