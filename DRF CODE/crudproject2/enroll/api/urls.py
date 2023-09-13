from django.db import router
from django.urls import path, include
from enroll.api import views
from rest_framework.routers import DefaultRouter


# Create Router Object
router = DefaultRouter()

# Register StudebtViewSet with Router
router.register('crud', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
