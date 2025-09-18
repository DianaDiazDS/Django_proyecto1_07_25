from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('mumero de telefono',  max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)
    class Meta: 
        permissions = [('can_change_category', 'Can change category')] 
def __str__(self):
    return self.name