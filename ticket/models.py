from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Review(models.Model):
    lucky = models.IntegerField(validators=[MinValueValidator(2),MaxValueValidator(77)])
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"This is {self.lucky}! I'n {self.name}"