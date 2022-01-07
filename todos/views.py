from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from items.models import Item
from priorities.models import Priority
from .models import Todo
from rest_framework import serializers, viewsets

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'is_complete')


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
