from django.contrib import admin
from teacherenroll.models import Teacher

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'teaching_exp', 'bio_data')


admin.site.register(Teacher, TeacherAdmin)