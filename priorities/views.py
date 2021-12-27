from rest_framework.response import Response
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view

from .models import Priority

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ('id', 'priority')


@api_view(['GET'])
def priorities(request):
    priorities = Priority.objects.all()
    serialized = PrioritySerializer(priorities, many = True)
    return Response(serialized.data)
