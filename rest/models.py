from django.db import models

# Create your models here.

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[("active", "Active"), ("inactive", "Inactive")])

    def __str__(self):
        return self.name