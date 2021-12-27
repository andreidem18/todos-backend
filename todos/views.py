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

class ItemSerializer(serializers.ModelSerializer):
    priority = PrioritySerializer(read_only=True)
    class Meta:
        model = Item
        fields = ('id', 'item', 'todo', 'priority')

class TodoSerializer(serializers.ModelSerializer):
    items = ItemSerializer(read_only=True, many=True)
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'deadline', 'items')


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def create(self, request, *args, **kwargs):
        todo = Todo.objects.create(
            title = request.data['title'], description = request.data['description'], deadline = request.data['deadline']
        )
        for i in request.data['items']:
            Item.objects.create(
                item = i['item'],
                todo = todo,
                priority = Priority.objects.get(id = i['priority'])
            )
        serialized = TodoSerializer(todo)
        return Response(status = status.HTTP_201_CREATED, data = serialized.data)
