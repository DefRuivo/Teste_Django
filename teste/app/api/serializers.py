from rest_framework import serializers
from app.models import customers_model


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = customers_model.Customers
        fields = '__all__'


class IDSerializer(serializers.ModelSerializer):
    class Meta:
        model = customers_model.Customers
        fields = '__all__'