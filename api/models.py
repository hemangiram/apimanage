from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Office(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    salary = models.CharField(max_length=10)


    def __str__(self):
        return self.name