from django.conf import settings
from django.db import models


class Kennel(models.Model):
    "Generated Model"
    kennel = models.ManyToManyField(
        "users.User",
        related_name="kennel_kennel",
    )


# Create your models here.
