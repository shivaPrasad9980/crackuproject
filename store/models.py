from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField( max_length=150)
    description = models.TextField()
    price = models.DecimalField( max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 