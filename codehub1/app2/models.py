from django.db import models

# Create your models here.

class FoodItem(models.Model):

    name=models.CharField(max_length=100)
    price=models.IntegerField()
    desc=models.CharField(max_length=200) 

    def __str__(self):
        return f"{self.name}"