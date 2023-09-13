from django.contrib import admin
from enroll.models import User

# Create your admi  here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')