from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

class Menus(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")
    #el primer atrobuto es la clase para que el modelo se conecte MenuCategory y la segunda es el tipo de relación
    def __str__(self):
        return f"{self.name} : {self.category_id.menu_category_name} - ${self.price}"