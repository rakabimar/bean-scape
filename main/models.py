from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=255)
    bitterness = models.IntegerField()
    
    @property
    def is_coffee_bitter(self):
        return self.bitterness > 5
