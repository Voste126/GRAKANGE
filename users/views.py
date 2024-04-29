from rest_framework import viewsets
from .models import Farmer, Farm
from .serializers import FarmerSerializer, FarmSerializer
from django.http import JsonResponse
from .models import Farmer
from .serializers import FarmerSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class FarmerViewSet(viewsets.ViewSet):
    #for the swagger UI
    @swagger_auto_schema(request_body=FarmerSerializer)
    def create(self, request):
        if request.method == 'POST':
            serializer = FarmerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=400)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID of the farmer", type=openapi.TYPE_INTEGER)
    ])
    def retrieve(self, request, pk):
        try:
            farmer = Farmer.objects.get(pk=pk)
        except Farmer.DoesNotExist:
            return JsonResponse({'error': 'Farmer not found'}, status=404)
        
        if request.method == 'GET':
            serializer = FarmerSerializer(farmer)
            return JsonResponse(serializer.data, status=200)

    @swagger_auto_schema(request_body=FarmerSerializer)
    def update(self, request, pk):
        try:
            farmer = Farmer.objects.get(pk=pk)
        except Farmer.DoesNotExist:
            return JsonResponse({'error': 'Farmer not found'}, status=404)
        
        if request.method == 'PUT':
            serializer = FarmerSerializer(farmer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=400)

    def list(self, request):
        queryset = Farmer.objects.all()
        serializer = FarmerSerializer(queryset, many=True)
        return JsonResponse(serializer.data,safe=False,status=200)

    def destroy(self, request, pk):
        try:
            farmer = Farmer.objects.get(pk=pk)
        except Farmer.DoesNotExist:
            return JsonResponse({'error': 'Farmer not found'}, status=404)
        
        if request.method == 'DELETE':
            farmer.delete()
            return JsonResponse({'message': 'Farmer deleted successfully'}, status=204)
        
class FarmViewSet(viewsets.ViewSet):
    #for the swagger UI
    @swagger_auto_schema(request_body=FarmSerializer)
    def create(self, request):
        if request.method == 'POST':
            serializer = FarmSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID of the farm", type=openapi.TYPE_INTEGER)
    ])
    def retrieve(self, request, pk):
        try:
            farm = Farm.objects.get(pk=pk)
        except Farm.DoesNotExist:
            return JsonResponse({'error': 'Farm not found'}, status=404)
        
        if request.method == 'GET':
            serializer = FarmSerializer(farm)
            return JsonResponse(serializer.data, status=200)
    @swagger_auto_schema(request_body=FarmSerializer)
    def update(self, request, pk):
        try:
            farm = Farm.objects.get(pk=pk)
        except Farm.DoesNotExist:
            return JsonResponse({'error': 'Farm not found'}, status=404)
        
        if request.method == 'PUT':
            serializer = FarmSerializer(farm, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)

    def list(self, request):
        queryset = Farm.objects.all()
        serializer = FarmSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False,status=200)
    
    def destroy(self, request, pk):
        try:
            farm = Farm.objects.get(pk=pk)
        except Farm.DoesNotExist:
            return JsonResponse({'error': 'Farm not found'}, status=404)
        
        if request.method == 'DELETE':
            farm.delete()
            return JsonResponse({'message': 'Farm deleted successfully'}, status=204)