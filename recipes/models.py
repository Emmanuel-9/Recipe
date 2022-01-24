from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    Title = models.CharField(max_length=25)
    Image = models.ImageField(default='food.jpeg',blank=True)
    Description = models.CharField(max_length=150)
    Instructions = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
   

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

class Profile(models.Model):
    username = models.CharField(max_length=50)
    profile_image = models.ImageField(default='food.jpeg',blank=True)
    recipe_count = models.IntegerField()
    email = models.EmailField()     

    def __str__(self):
        return self.username

    def save_recipe(self, **kwargs):
        super().save()

    def del_profile(self):
        self.delete()
   