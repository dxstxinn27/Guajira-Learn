from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MyApps.discusiones.models import Foro, Mensaje

class ForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foro
        fields = "__all__"

class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = "__all__"