from rest_framework import serializers
from kennel.models import Kennel


class KennelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kennel
        fields = "__all__"
