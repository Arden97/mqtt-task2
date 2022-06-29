from django.db import models

class Cryptocurrency(models.Model):
    id = models.CharField(max_length=15,primary_key = True)
    rank = models.PositiveIntegerField()
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=15)
    supply = models.FloatField()
    marketCapUsd = models.FloatField()
    volumeUsd24Hr = models.FloatField()
    priceUsd = models.FloatField()
    changePercent24Hr = models.FloatField()
    vwap24Hr = models.FloatField()
    
