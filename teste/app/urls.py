from django.urls import path, include
from rest_framework import routers
from app.api import viewsets as apiviewsets

route = routers.DefaultRouter()

route.register(r'customers', apiviewsets.AllViewSets, basename='customers')


urlpatterns = [
    path('', include(route.urls))
]
