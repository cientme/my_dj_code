from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from api.auth import CustomAuthToken
# Create Router Object.
router = DefaultRouter()

# Register StudentApi with Router.
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', CustomAuthToken.as_view()),
]
 
 # To install obtain_auth_token using command pip install httpie