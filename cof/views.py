from django.shortcuts import render
from cof import models
from cof.serializers import MachineSerializer,PodSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
import django_filters.rest_framework


class MachineList(generics.ListAPIView):
    queryset = models.Machine.objects.all()
    serializer_class = MachineSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['product_type', 'water_line_compitable']


class PodList(generics.ListAPIView):
    queryset = models.Pod.objects.all()
    serializer_class = PodSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['product_type', 'flavor','pack_size']

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset


