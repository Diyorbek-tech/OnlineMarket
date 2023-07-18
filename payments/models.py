from django.db import models
from base.BaseModel import Base_Model
# Create your models here.
from accounts.models import  User

import uuid
'''
6 12%
12 25%
18 38%
24 50%
'''
class Payment(Base_Model):

    charge_id=models.UUIDField(default=uuid.uuid4,unique=True)
    user=models.ForeignKey(to=User,on_delete=models.RESTRICT)
    amount=models.IntegerField()

class Coupon(Base_Model):

    coupon_code=models.UUIDField(default=uuid.uuid4,unique=True)
    amount=models.IntegerField()
    valid_from=models.DateField()
    valid_to=models.DateField()

    active=models.BooleanField(default=False)

class Credit_card(Base_Model):
    card_types=(
        ('mastercard','mastercard'),
        ('visa','visa'),
        ('humo','humo'),
        ('uzcard','uzcard'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    card_type=models.CharField(max_length=15,choices=card_types)
    card_num=models.IntegerField()
    card_ccv=models.IntegerField(blank=True,null=True)
    valid_date=models.DateField()
    is_valid=models.BooleanField(default=True)

def Split_the_bill(price,month,gavep=None):
    if gavep:
        price-=gavep
    match month:
        case 3:return price/3
        case 6:return (price*1.12)/6
        case 12:return (price*1.25)/12
        case 18:return (price*1.38)/18
        case 24:return (price*1.50)/24
        case _ :return None










