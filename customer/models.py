
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=120)


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    is_married = models.BooleanField()
    bio = models.TextField(max_length=4096,blank=True,null=True)
    height = models.FloatField()
    birthday = models.DateField(blank=True,null=True)
    birthtime = models.TimeField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} ! {self.email}"

class Parents(models.Model):
    person= models.OneToOneField(Person, on_delete=models.SET_NULL, blank=True, null=True)
    father_name = models.CharField(max_length = 80)
    mother_name = models.CharField(max_length = 80)

class Friend (models.Model):
    person = models.ForeignKey(Person,on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=60)
    addres = models.CharField(max_length = 60)
    mobail = models.CharField(max_length = 60)


    def __str__(self):
        return f"{self.name} ! {self.person.name if self.person else "no friend"}"

