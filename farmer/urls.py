from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import FarmerViewSet, FarmViewSet
from retailers.views import CustomerViewSet, BusinessViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
# """
# URL configuration for farmer project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

schema_view = swagger_get_schema_view(
    openapi.Info(
        title= "Grakange API",
        default_version='1.0.0',
        description="API for Django project Grakange",
    ),
    public=True,
)

router = DefaultRouter()
router.APIRootView.__doc__ = "Welcome to Grakange API"
router.register(r'farmers', FarmerViewSet, basename='farmer')
router.register(r'farm', FarmViewSet, basename='farm')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'business', BusinessViewSet, basename='business')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('',include('retailers.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
]



