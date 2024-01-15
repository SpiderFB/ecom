from django.db import models

# Create your models here.
class allitem(models.Model):
        product_id = models.IntegerField(unique= 1, primary_key = 1)
        product_name = models.CharField(max_length=20)
        product_description = models.CharField(max_length=50)
        product_category = models.CharField(max_length=10)
        product_price = models.IntegerField()
        product_quantity = models.IntegerField()
        # product_image = models.ImageField(upload_to='static/images/',default='default_image.jpg')
        # product_image = models.ImageField(upload_to='static/images/')
        product_image = models.ImageField(upload_to='product')
        def __str__(self) -> str:
            return (f"{self.product_id}")