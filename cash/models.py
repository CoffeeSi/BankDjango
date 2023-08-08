from django.db import models

# Create your models here.

class Money(models.Model):
    cardh = models.CharField(max_length=8)
    money = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cardh
    
    