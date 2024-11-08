from dataclasses import field
from statistics import mode
from rest_framework import serializers
from MyApps.usuarios.models import Docente, Estudiante, Tutor, HorarioDisponibilidad

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = "__all__"

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = "__all__"

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = "__all__"

class HorarioDisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioDisponibilidad
        fields = "__all__"