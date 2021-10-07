from django.db import models
from django.utils import timezone

class Person(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length = 200, unique=True)
    register_date = models.DateTimeField('date register', default=timezone.now)

    def __str__(self):
        return self.user_name
