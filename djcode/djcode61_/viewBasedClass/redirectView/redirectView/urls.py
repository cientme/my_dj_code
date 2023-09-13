"""redirectView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(template_name='school/home.html'), name='blankhome'),
    # path('home/', views.RedirectView.as_view(url='/'), name='home'),
    path('home/', views.RedirectView.as_view(url='/something/'), name='home2'),
    # path('index/', views.RedirectView.as_view(url='/'), name='index'),

    path('index/', views.RedirectView.as_view(pattern_name='home2'), name='index'),

    # path('youtube/', views.RedirectView.as_view(url='http://www.youtube.com'), name='go-to-youtube'),
    path('youtube/', views.YouTubeRedirectView.as_view(), name='youtube'),

    path('you/<int:pk>/', views.YouRedirectView.as_view(), name='you'),

    path('<int:pk>/', views.TemplateView.as_view(template_name='school/home.html'), name='minindex'),

    # path('you/<slug:post>/', views.YouRedirectView.as_view(), name='you'),

    # path('<slug:post>/', views.TemplateView.as_view(template_name='school/home.html'), name='minindex'),

]
