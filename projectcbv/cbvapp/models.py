from django.db import models
from django.urls import reverse

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("cbvapp:detail", kwargs={"pk": self.pk})


class Car(models.Model):
    brand = models.CharField(max_length=256)
    license_plate = models.CharField(max_length=256)
    manufacturing_year = models.PositiveIntegerField()
    
    
    def __str__(self):
        return self.brand
    
    # def get_absolute_url(self):
    #     return reverse("cbvapp:detail", kwargs={"pk": self.pk})


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
