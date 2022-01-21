from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    Title = models.CharField(max_length=25)
    Image = models.ImageField(null=True)
    Description = models.CharField(max_length=150)
    Instructions = models.TextField()
    pub_date = models.DateTimeField()
   

    def __str__(self):
        return self.Title


    def save_recipe(self, **kwargs):
        super().save()

    def del_recipe(self):
        self.delete()    

class User(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.name

    def save_user(self):
        self.save()

    def del_user(self):
        self.delete()