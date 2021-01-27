from rest_framework import serializers
from .models import Mods


# output serializer class for  'Mods' model
class ModSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mods
        fields = '__all__'
