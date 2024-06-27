from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=40,blank=True)
    locationh = models.CharField(max_length=120,blank=True)
    birth_day = models.DateField(blank=True,null=True)
    father_name = models.CharField(max_length=409,blank=True,null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance,crated,**kwargs):
    if crated:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance,crated,**kwargs):
    instance.profile.save()
