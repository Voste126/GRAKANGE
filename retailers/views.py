# Create your views here.
## class based views for customers
from rest_framework import viewsets
from .models import Business, Customer
from .serializers import BusinessSerializer, CustomerSerializer
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema  
from drf_yasg import openapi


class CustomerViewSet(viewsets.ViewSet):
    ##for the swagger UI 
    @swagger_auto_schema(request_body=CustomerSerializer)
    def create(self, request):
        if request.method == 'POST':
            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=400)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID of the customer", type=openapi.TYPE_INTEGER)
    ])
    def retrieve(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)
        
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return JsonResponse(serializer.data, status=200)

    @swagger_auto_schema(request_body=CustomerSerializer)
    def update(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)
        
        if request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)

    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return JsonResponse(serializer.data,safe=False,status=200)

    def destroy(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)
        
        if request.method == 'DELETE':
            customer.delete()
            return JsonResponse({'message': 'Customer deleted successfully'}, status=204)
        

class BusinessViewSet(viewsets.ViewSet):
    @swagger_auto_schema(request_body=BusinessSerializer)
    def create(self, request):
        if request.method == 'POST':
            serializer = BusinessSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=400)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID of the customer", type=openapi.TYPE_INTEGER)
    ])
    def retrieve(self, request, pk):
        try:
            business = Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            return JsonResponse({'error': 'Business not found'}, status=404)
        
        if request.method == 'GET':
            serializer = BusinessSerializer(business)
            return JsonResponse(serializer.data, status=200)

    @swagger_auto_schema(request_body=BusinessSerializer)
    def update(self, request, pk):
        try:
            business = Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            return JsonResponse({'error': 'Business not found'}, status=404)
        
        if request.method == 'PUT':
            serializer = BusinessSerializer(business, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)

    def list(self, request):
        queryset = Business.objects.all()
        serializer = BusinessSerializer(queryset, many=True)
        return JsonResponse(serializer.data,safe=False,status=200)

    def destroy(self, request, pk):
        try:
            business = Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            return JsonResponse({'error': 'Business not found'}, status=404)
        
        if request.method == 'DELETE':
            business.delete()
            return JsonResponse({'message': 'Business deleted successfully'}, status=204)