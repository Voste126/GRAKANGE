from django.urls import path
from retailers.views import CustomerViewSet, BusinessViewSet

urlpatterns = [
    path('customers/', CustomerViewSet.as_view({
        'post': 'create',
        'get': 'list'
    })),
    path('customers/<int:pk>/', CustomerViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('business/', BusinessViewSet.as_view({
        'post': 'create',
        'get': 'list'
    })),
    path('business/<int:pk>/', BusinessViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
