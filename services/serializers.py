from rest_framework import serializers

from services.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'email', 'phone_number',
                  'language', 'currency')
        model = Provider
