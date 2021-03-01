from rest_framework import viewsets
from app.api import serializers
from app.models.customers_model import Customers


class AllViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.AppSerializer
    queryset = Customers.objects.all()


class IdViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.IDSerializer

    def get_queryset(self):
        id = self.request.user
        return Customers.objects.filter(id=id)