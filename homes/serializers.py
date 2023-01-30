from rest_framework import serializers
from .models import Home


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'street_address', 'city', 'state', 'zip', 'square_feet', 'description', 'created_at')
        model = Home
