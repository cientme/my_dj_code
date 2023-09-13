from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    teaching_exp = models.CharField(max_length=300)
    bio_data = models.CharField(max_length=100)

    def __str__(self):
        self.full_name = self.first_name + ' ' + self.last_name
        return self.full_name