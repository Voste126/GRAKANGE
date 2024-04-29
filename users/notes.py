# Create your views here.
# # function based views for farmers
# def create_farmer(request):
#     if request.method == 'POST':
#         serializer = FarmerSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# def get_farmer(request, id):
#     try:
#         farmer = Farmer.objects.get(pk=id)
#     except Farmer.DoesNotExist:
#         return JsonResponse({'error': 'Farmer not found'}, status=404)
    
#     if request.method == 'GET':
#         serializer = FarmerSerializer(farmer)
#         return JsonResponse(serializer.data, status=200)

# def update_farmer(request, id):
#     try:
#         farmer = Farmer.objects.get(pk=id)
#     except Farmer.DoesNotExist:
#         return JsonResponse({'error': 'Farmer not found'}, status=404)
    
#     if request.method == 'PUT':
#         serializer = FarmerSerializer(farmer, data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

# def delete_farmer(request, id):
#     try:
#         farmer = Farmer.objects.get(pk=id)
#     except Farmer.DoesNotExist:
#         return JsonResponse({'error': 'Farmer not found'}, status=404)
    
#     if request.method == 'DELETE':
#         farmer.delete()
#         return JsonResponse({'message': 'Farmer deleted successfully'}, status=204)