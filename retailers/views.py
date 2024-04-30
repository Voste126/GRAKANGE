# Create your views here.
## class based views for customers
from rest_framework import viewsets,status
from .models import Business, Customer
from .serializers import BusinessSerializer, CustomerSerializer
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema  
from drf_yasg import openapi
from rest_framework.response import Response


class CustomerViewSet(viewsets.ViewSet):
    ##for the swagger UI 
    @swagger_auto_schema(request_body=CustomerSerializer)
    def create(self, request):
        if request.method == 'POST':
            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID of the customer", type=openapi.TYPE_INTEGER)
    ])
    def retrieve(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CustomerSerializer)
    def update(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data,safe=False,status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'DELETE':
            customer.delete()
            return Response({'message': 'Customer deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        

class BusinessViewSet(viewsets.ViewSet):
    @swagger_auto_schema(request_body=BusinessSerializer)
    def create(self, request):
        if request.method == 'POST':
            serializer = BusinessSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID of the customer", type=openapi.TYPE_INTEGER)
    ])
    def retrieve(self, request, pk):
        try:
            business = Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            return Response({'error': 'Business not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = BusinessSerializer(business)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=BusinessSerializer)
    def update(self, request, pk):
        try:
            business = Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            return Response({'error': 'Business not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'PUT':
            serializer = BusinessSerializer(business, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Business.objects.all()
        serializer = BusinessSerializer(queryset, many=True)
        return Response(serializer.data,safe=False,status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        try:
            business = Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            return Response({'error': 'Business not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'DELETE':
            business.delete()
            return Response({'message': 'Business deleted successfully'}, status=status.HTTP_204_NO_CONTENT)