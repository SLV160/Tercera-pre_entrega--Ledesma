from django.db import models

class Clase1(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()

class Clase2(models.Model):
    campo3 = models.CharField(max_length=150)

class Clase3(models.Model):
    campo4 = models.CharField(max_length=200)
    campo5 = models.BooleanField()
