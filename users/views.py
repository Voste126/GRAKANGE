from rest_framework import viewsets,status
from .models import Farmer, Farm
from .serializers import FarmerSerializer, FarmSerializer
from django.http import JsonResponse
from .models import Farmer
from .serializers import FarmerSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response


class FarmerViewSet(viewsets.ViewSet):
    #for the swagger UI
    @swagger_auto_schema(request_body=FarmerSerializer)
    def create(self, request):
        if request.method == 'POST':
            serializer = FarmerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID of the farmer", type=openapi.TYPE_INTEGER)
    ])
    def retrieve(self, request, pk):
        try:
            farmer = Farmer.objects.get(pk=pk)
        except Farmer.DoesNotExist:
            return Response({'error': 'Farmer not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = FarmerSerializer(farmer)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=FarmerSerializer)
    def update(self, request, pk):
        try:
            farmer = Farmer.objects.get(pk=pk)
        except Farmer.DoesNotExist:
            return Response({'error': 'Farmer not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'PUT':
            serializer = FarmerSerializer(farmer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Farmer.objects.all()
        serializer = FarmerSerializer(queryset, many=True)
        return Response(serializer.data, safe=False,status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        try:
            farmer = Farmer.objects.get(pk=pk)
        except Farmer.DoesNotExist:
            return Response({'error': 'Farmer not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'DELETE':
            farmer.delete()
            return Response({'message': 'Farmer deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        
class FarmViewSet(viewsets.ViewSet):
    #for the swagger UI
    @swagger_auto_schema(request_body=FarmSerializer)
    def create(self, request):
        if request.method == 'POST':
            serializer = FarmSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID of the farm", type=openapi.TYPE_INTEGER)
    ])
    def retrieve(self, request, pk):
        try:
            farm = Farm.objects.get(pk=pk)
        except Farm.DoesNotExist:
            return Response({'error': 'Farm not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = FarmSerializer(farm)
            return Response(serializer.data, status=status.HTTP_200_OK)
    @swagger_auto_schema(request_body=FarmSerializer)
    def update(self, request, pk):
        try:
            farm = Farm.objects.get(pk=pk)
        except Farm.DoesNotExist:
            return Response({'error': 'Farm not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'PUT':
            serializer = FarmSerializer(farm, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Farm.objects.all()
        serializer = FarmSerializer(queryset, many=True)
        return Response(serializer.data,safe=False, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        try:
            farm = Farm.objects.get(pk=pk)
        except Farm.DoesNotExist:
            return Response({'error': 'Farm not found'}, status=status.HTTP_404_NOT_FOUND)
        if request.method == 'DELETE':
            farm.delete()
            return  Response({'message': 'Farm deleted successfully'}, status=status.HTTP_204_NO_CONTENT)