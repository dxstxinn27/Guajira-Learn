from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from MyApps.discusiones.models import Foro, Mensaje
from MyApps.discusiones.serializers import ForoSerializer, MensajeSerializer

# Create your views here.


class ForoList(APIView):
    """
    Lista de Asignaturas
    """

    def get(self, request, format=None):
        foros = Foro.objects.all()
        serializer = ForoSerializer(foros, many=True)
        return Response({"foros":serializer.data})

    def post(self, request, format=None):
        serializer = ForoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForoDetail(APIView):
    """
    Retrieve, update or delete de los foros por pk
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Foro.objects.get(pk=pk)
        except Foro.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        foro = self.get_object(pk)
        serializer = ForoSerializer(foro)
        return Response({"foro":serializer.data})

    def put(self, request, pk, format=None):
        foro = self.get_object(pk)
        serializer = ForoSerializer(foro, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        foro = self.get_object(pk)
        serializer = ForoSerializer(foro,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        foro = self.get_object(pk)
        foro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MensajeList(APIView):
    """
    Lista de Mensajes
    """

    def get(self, request, format=None):
        mensajes = Mensaje.objects.all()
        serializer = MensajeSerializer(mensajes, many=True)
        return Response({"temas":serializer.data})

    def post(self, request, format=None):
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MensajeDetail(APIView):
    """
    Retrieve, update or delete de los mensajes por pk
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Mensaje.objects.get(pk=pk)
        except Mensaje.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        mensaje = self.get_object(pk)
        serializer = MensajeSerializer(mensaje)
        return Response({"mensaje":serializer.data})

    def put(self, request, pk, format=None):
        mensaje = self.get_object(pk)
        serializer = MensajeSerializer(mensaje, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        mensaje = self.get_object(pk)
        serializer = MensajeSerializer(mensaje,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        mensaje = self.get_object(pk)
        mensaje.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
