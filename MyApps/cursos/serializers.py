from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MyApps.cursos.models import Asignatura, Tema

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = "__all__"

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = "__all__"