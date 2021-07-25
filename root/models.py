from django.db import models

# Create your models here.

class Cultivo(models.Model):
    name = models.CharField( max_length=50)
    # fitossa
    fitomassa = models.FloatField()
    # kg por co2
    kgco2 = models.FloatField()
    # planta por ha
    plha = models.IntegerField(default=0)
    # meses de cultivo
    meses = models.IntegerField()

    def __str__(self):
        return self.name

class Foresta(models.Model):
    name = models.CharField( max_length=50)
    # kg por co2
    kgco2 = models.FloatField()
    def __str__(self):
        return self.name

