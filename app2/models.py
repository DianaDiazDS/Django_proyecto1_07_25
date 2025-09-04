from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} : {self.cuisine} - ${self.price}"

class Person(models.Model): 
    name = models.CharField(max_length=20) 
    email = models.EmailField()
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=20) 



class Customer(models.Model): 
    name = models.CharField(max_length=255) 

class Vehicle(models.Model): 
    name = models.CharField(max_length=255) 
    customer = models.ForeignKey( 
        Customer, 
        on_delete=models.CASCADE, 
        related_name='Vehicle' 
    ) 