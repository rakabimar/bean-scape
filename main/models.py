import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=255)
    bitterness = models.IntegerField()
    
    @property
    def is_coffee_bitter(self):
        return self.bitterness > 5
