from django.shortcuts import render
from rest_framework import generics, status, mixins

from services.models import Area, Provider
from services.serializers import AreaSerializer, ProviderSerializer
from django.contrib.gis.geos import fromstr


class ProviderView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProviderDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AreaView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    def get_queryset(self):
        queryset = Area.objects.all()
        provider_id = self.request.GET.get("provider_id")
        if provider_id:
            queryset = queryset.filter(provider_id=provider_id)
        point_str = self.request.GET.get("point")
        if point_str:
            point = fromstr(point_str)
            queryset = queryset.filter(region__contains=point)
        return queryset.order_by('-created_at')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AreaDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
