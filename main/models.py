from __future__ import unicode_literals
from django.db import models

# Create your models here.

class User(models.Model):
    email = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return self.first_name

    
   