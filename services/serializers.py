from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from services.models import Provider, Area


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Provider


class AreaSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(required=False)
    provider_id = serializers.IntegerField(write_only=True)

    class Meta:
        fields = '__all__'
        model = Area
        geo_field = 'region'
