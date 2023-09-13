from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Create Your Router Object
router = DefaultRouter()

# Register Router 
router.register('studentapi', views.StudentModelViewSet, basename='stuapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
  
]
