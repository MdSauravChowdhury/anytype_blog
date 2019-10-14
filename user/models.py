from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmailSubcribe(models.Model):
    email = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return self.email