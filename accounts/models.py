from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN='ADMIN','ADMIN'
        SELLER='SELLER','SELLER'
        CUSTOMER='CUSTOMER','CUSTOMER'

    base_role=Role.ADMIN

    role=models.CharField(max_length=10,choices=Role.choices)

    def save(self,*args,**kwargs):
        if not self.pk:
            self.role=self.base_role
            return super().save(*args,**kwargs)

class Seller(User):
    base_role = User.Role.SELLER
    class Meta():
        proxy=True

class Customer(User):
    base_role = User.Role.CUSTOMER
    class Meta():
        proxy=True




















"""
Admin

Sales

Customer

"""

