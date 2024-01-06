from django.db import models

# Create your models here.
class allitem(models.Model):
        var1 = models.CharField(max_length=20)
        var2 = models.IntegerField()
        def __str__(self) -> str:
            return (f"{self.var1} {self.var2}")