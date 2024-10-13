from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    fname = models.CharField(max_length=200, default="fname")
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    file = models.FileField()

class Car(models.Model):
    car_name = models.CharField(max_length=200)
    speed = models.IntegerField(default=50)
    
    def __str__(self):
        return f"model: {self.car_name} and speed: {self.speed}"
