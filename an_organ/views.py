from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import AnalyticalMethod, Instrument
from .serializers import AnalyticalMethodSerializer, InstrumentSerializer
from .permissions import IsOwnerOrReadOnly


class AnalyticalMethodViewSet(viewsets.ModelViewSet):
    queryset = AnalyticalMethod.objects.all().order_by("-method_name")
    serializer_class = AnalyticalMethodSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all().order_by("-instrument_id")
    serializer_class = InstrumentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def instrument_detail(self, request, pk=None):
        instrument = self.get_object()
        serializer = self.get_serializer(instrument)
        return Response(serializer.data)

    def perform_create(self, serializer):
        if 'owner' in serializer.validated_data:
            del serializer.validated_data['owner']
        serializer.save()

# class AnalyticalMethodRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = AnalyticalMethod.objects.all()
#     serializer_class = AnalyticalMethodSerializer
