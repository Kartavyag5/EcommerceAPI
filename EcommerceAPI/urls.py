from django.contrib import admin
from django.urls import include, path

from api.views import RegistrationAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api-auth/',include('rest_framework.urls')),
    
]
