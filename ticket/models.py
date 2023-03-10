from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

# Create your models here.


class Ticket(models.Model):
    # DUNDER METHOD RETURNS WHEREVER THE OBJECT IS CALLED AS-IS
    def __str__(self):
        return f"""
        #{self.pk} by {self.author} has {self.priority} priority
        """

    # HIDDEN INPUT FIELDS SO IT BECOMES EASIER TO IDENTIFY USER (GRABBED FROM HIM/HER BEHIND THE SCENES)
    author = models.CharField(max_length=80, default='John Smith')
    manager = models.CharField(max_length=80, default='Sam Adams')
    department = models.CharField(max_length=80, default='Finance')
    date = models.DateTimeField(auto_now=True)
    # PUBLICLY DISPLAYED FIELDS
    priority = models.CharField(max_length=6, default='Low')
    evidence = models.ImageField(upload_to="images",
                                 default='https://oncall258.com/wp-content/uploads/2015/03/iStock_000054981982_Small.jpg')
    comment = models.CharField(max_length=5000, default='Lorem Ipsum')
