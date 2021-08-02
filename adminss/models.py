from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField


# Create your models here.

ROLE_CHOICES = (
    ('Admin','Admin'),
    ('Agent','Agent'),
    ('Customer','Customer')
)
class Roles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.CharField(choices=ROLE_CHOICES, max_length=15, null=True)

    def __str__(self):
        return str(self.user.username)

    
