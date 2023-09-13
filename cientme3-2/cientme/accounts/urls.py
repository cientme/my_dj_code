from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change-password-with-old-password/', views.user_change_password_with_old_password, name='change-password-with-old-password'),
    path('change-password/', views.user_change_password, name='change-password'),
    path('forget-password/', views.forget_password, name='forget-password'),
    
]
