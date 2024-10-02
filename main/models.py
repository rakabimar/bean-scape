import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    # Define choices as class attributes
    BEVERAGE = 'BEV'
    BEANS = 'BNS'
    
    CATEGORY_CHOICES = [
        (BEVERAGE, 'Beverage'),
        (BEANS, 'Beans'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES,
        default=BEVERAGE,
    )
    bitterness = models.IntegerField(
        validators=[
            MinValueValidator(1, 'Bitterness must be at least 1'),
            MaxValueValidator(10, 'Bitterness cannot exceed 10')
        ],
        default=5
    )
    
    @property
    def is_coffee_bitter(self):
        return self.bitterness > 5
    
    @property
    def bitterness_width(self):
        return self.bitterness * 10