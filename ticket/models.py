from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

# Create your models here.


class Ticket(models.Model):
    def __str__(self):
        return f"""
        #{self.pk} by {self.author} has {self.priority} priority
        """

    priority = models.CharField(max_length=6, default='Low')
    author = models.CharField(max_length=80, default='John Smith')
    date = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=5000, default='Lorem Ipsum')
