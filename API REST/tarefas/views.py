from django.shortcuts import render
from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer

# Create your views here.

class TarefaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite operações CRUD em tarefas.
    """
    queryset = Tarefa.objects.all().order_by('-data_criacao')
    serializer_class = TarefaSerializer
