from django.db import models
import django.db
# Create your models here.
import threading

class Item(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    desc=models.CharField(max_length=200,blank=True) 
    image=models.CharField(max_length=200,default="not found")

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        print(f"[save] Running in thread: {threading.get_ident()}")
        print("in save")
        
        # Custom logic before saving
        if not self.desc:
          	# Assign a default name if none is provided
            self.desc = "Default Codehub"
        # Call the original save() method
        super().save(*args, **kwargs)
        
        # Custom logic after saving
        print(f'{self.desc} has been saved!') 