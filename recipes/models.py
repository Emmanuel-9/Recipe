#from dis import Instruction
#from turtle import title
from django.db import models

# Create your models here.
class Recipe(models.Model):
    Title = models.CharField(max_length=25)
    Description = models.CharField(max_length=150)
    Instructions = models.TextField()
    pub_date = models.DateTimeField()

    def __str(self):
        return self.Title

