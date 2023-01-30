from django.contrib.auth import get_user_model
from django.db import models


class Home(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    street_address = models.CharField(max_length=256)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    zip = models.IntegerField(default=0)
    square_feet = models.IntegerField(default=0)
    description = models.TextField(default='N/A')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.street_address
