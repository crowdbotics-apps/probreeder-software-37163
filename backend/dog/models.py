from django.conf import settings
from django.db import models


class Dog(models.Model):
    "Generated Model"
    dog = models.ManyToManyField(
        "kennel.Kennel",
        related_name="dog_dog",
    )


# Create your models here.
