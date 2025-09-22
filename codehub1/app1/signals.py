# code
import threading
from django.db.models.signals import post_save,pre_save
from .models import Item
from django.dispatch import receiver


@receiver(pre_save, sender=Item) 
def save_profile(sender, instance, **kwargs):
        print("before saving")
        print("sender",sender)
        print("instance",instance)
        print(f"[reciever] Running in thread: {threading.get_ident()}")
        for key,value in kwargs.items():
                print(key,value) 
        

@receiver(post_save, sender=Item) 
def save_profile(sender, instance, **kwargs):
        print("after saving")
        