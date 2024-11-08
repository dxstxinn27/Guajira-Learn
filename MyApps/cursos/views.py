from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from MyApps.cursos.models import Asignatura, Tema
from MyApps.cursos.serializers import AsignaturaSerializer, TemaSerializer

# Create your views here.


class AsignaturaList(APIView):
    """
    Lista de Asignaturas
    """

    def get(self, request, format=None):
        asignaturas = Asignatura.objects.all()
        # data = {"results": list(clientes.values("nombreCliente", "direccionCliente", "telefonoCliente", "correoCliente", "passwordCliente"))}
        # print(data)
        # return JsonResponse(data)
        serializer = AsignaturaSerializer(asignaturas, many=True)
        return Response({"asignaturas":serializer.data})

    def post(self, request, format=None):
        serializer = AsignaturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AsignaturaDetail(APIView):
    """
    Retrieve, update or delete de los asignaturas por pk
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Asignatura.objects.get(pk=pk)
        except Asignatura.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        asignatura = self.get_object(pk)
        serializer = AsignaturaSerializer(asignatura)
        return Response({"asignatura":serializer.data})

    def put(self, request, pk, format=None):
        asignatura = self.get_object(pk)
        serializer = AsignaturaSerializer(asignatura, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        asignatura = self.get_object(pk)
        serializer = AsignaturaSerializer(asignatura,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        asignatura = self.get_object(pk)
        asignatura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TemaList(APIView):
    """
    Lista de Temas
    """

    def get(self, request, format=None):
        temas = Tema.objects.all()
        serializer = TemaSerializer(temas, many=True)
        return Response({"temas":serializer.data})

    def post(self, request, format=None):
        serializer = TemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TemaDetail(APIView):
    """
    Retrieve, update or delete de los temas por pk
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Tema.objects.get(pk=pk)
        except Tema.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tema = self.get_object(pk)
        serializer = TemaSerializer(tema)
        return Response({"tema":serializer.data})

    def put(self, request, pk, format=None):
        tema = self.get_object(pk)
        serializer = TemaSerializer(tema, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        tema = self.get_object(pk)
        serializer = TemaSerializer(tema,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        tema = self.get_object(pk)
        tema.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
