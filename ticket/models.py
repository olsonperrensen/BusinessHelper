from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Ticket(models.Model):
    def __str__(self):
        return f"""
        #{self.pk} has {self.priority} priority
        """

    priority = models.CharField(max_length=6)
    comment = models.CharField(max_length=5000)
