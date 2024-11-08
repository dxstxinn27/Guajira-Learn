from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from MyApps.usuarios.models import Docente, Estudiante, Tutor, HorarioDisponibilidad
from MyApps.usuarios.serializers import DocenteSerializer, EstudianteSerializer, TutorSerializer, HorarioDisponibilidadSerializer
from django.contrib.auth.hashers import check_password

class EstudianteLoginView(APIView):
    def post(self, request):
        correo = request.data.get('correo')
        contraseña = request.data.get('password')

        try:
            estudiante = Estudiante.objects.get(correo=correo)
            
            # Imprimir los valores para verificar la comparación
            print(f"Contraseña ingresada: {contraseña}")
            print(f"Contraseña almacenada: {estudiante.contraseña}")

            # Comparación directa de texto plano
            if contraseña == estudiante.contraseña:
                print("Contraseña correcta.")
                return Response({"message": "Autenticado correctamente"}, status=status.HTTP_200_OK)
            else:
                print("Contraseña incorrecta.")
                return Response({"message": "Contraseña incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)
                
        except Estudiante.DoesNotExist:
            print("Estudiante no encontrado.")
            return Response({"message": "Estudiante no encontrado"}, status=status.HTTP_404_NOT_FOUND)

class DocenteList(APIView):

    def get(self, request, format=None):
        docentes = Docente.objects.all()
        serializer = DocenteSerializer(docentes, many=True)
        return Response({"docentes":serializer.data})

    def post(self, request, format=None):
        serializer = DocenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocenteDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Docente.objects.get(pk=pk)
        except Docente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        docente = self.get_object(pk)
        serializer = DocenteSerializer(docente)
        return Response({"docente":serializer.data})

    def put(self, request, pk, format=None):
        docente = self.get_object(pk)
        serializer = DocenteSerializer(docente, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        docente = self.get_object(pk)
        serializer = DocenteSerializer(docente,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        docente = self.get_object(pk)
        docente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EstudianteList(APIView):

    def get(self, request, format=None):
        estudiantes = Estudiante.objects.all()
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response({"estudiantes":serializer.data})

    def post(self, request, format=None):
        serializer = EstudianteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstudianteDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Estudiante.objects.get(pk=pk)
        except Estudiante.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        estudiante = self.get_object(pk)
        serializer = EstudianteSerializer(estudiante)
        return Response({"estudiante":serializer.data})

    def put(self, request, pk, format=None):
        estudiante = self.get_object(pk)
        serializer = EstudianteSerializer(estudiante, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        estudiante = self.get_object(pk)
        serializer = EstudianteSerializer(estudiante,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        estudiante = self.get_object(pk)
        estudiante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TutorList(APIView):

    def get(self, request, format=None):
        tutor = Tutor.objects.all()
        serializer = TutorSerializer(tutor, many=True)
        return Response({"tutor":serializer.data})

    def post(self, request, format=None):
        serializer =TutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TutorDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Tutor.objects.get(pk=pk)
        except Tutor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tutor = self.get_object(pk)
        serializer = TutorSerializer(tutor)
        return Response({"tutor":serializer.data})

    def put(self, request, pk, format=None):
        tutor = self.get_object(pk)
        serializer = TutorSerializer(tutor, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        tutor = self.get_object(pk)
        serializer = TutorSerializer(tutor,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        tutor = self.get_object(pk)
        tutor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class HorarioDisponibilidadList(APIView):

    def get(self, request, format=None):
        horario = HorarioDisponibilidad.objects.all()
        serializer = HorarioDisponibilidadSerializer(horario, many=True)
        return Response({"horario":serializer.data})

    def post(self, request, format=None):
        serializer = HorarioDisponibilidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HorarioDisponibilidadDetail(APIView):
    
    def get_object(self, pk):
        try:
            return HorarioDisponibilidad.objects.get(pk=pk)
        except HorarioDisponibilidad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        horario = self.get_object(pk)
        serializer = HorarioDisponibilidadSerializer(horario)
        return Response({"horario":serializer.data})

    def put(self, request, pk, format=None):
        horario = self.get_object(pk)
        serializer = HorarioDisponibilidadSerializer(horario, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        horario = self.get_object(pk)
        serializer = HorarioDisponibilidadSerializer(horario,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        horario = self.get_object(pk)
        horario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)