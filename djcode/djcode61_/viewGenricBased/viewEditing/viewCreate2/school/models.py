from django.db import models
from django.urls import reverse

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)

    # def get_absolute_url(self):
    #     return reverse('thankyou')

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    