from django.urls import path
from users.views import FarmerViewSet, FarmViewSet

urlpatterns = [
    path('farmers/', FarmerViewSet.as_view({
        'post': 'create',
        'get': 'list'
    })),
    path('farmers/<int:pk>/', FarmerViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('farm/', FarmViewSet.as_view({
        'post': 'create',
        'get': 'list'
    })),
    path('farm/<int:pk>/', FarmViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]