from django.db import models

# Create your models here.
class CoinName(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    entry = models.FloatField(max_length=20, blank=True,null=True)
    
    def __str__(self):
        return self.name