from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"ID: {self.id} Name: {self.name} \n"


class Car(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id} Name: {self.name} Brand: {self.brand} \n"


