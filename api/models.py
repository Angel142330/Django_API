from django.db import models

# Create your models here.

class Programador(models.Model):
   name=models.CharField(max_length=50)
   age=models.IntegerField()
   language=models.CharField(max_length=50)
   #created=models.DateTimeField(auto_now_add=True)
   