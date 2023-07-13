from accounts.models import  User
from django.db import models
from base.BaseModel import Base_Model
'''
Market
Category
Sub_Category
product
Images
'''

class Size(Base_Model):
    sub_cat=models.ForeignKey("Sub_Category",on_delete=models.CASCADE)
    size=models.CharField(max_length=15)

class Category(Base_Model):
    cat_name=models.CharField(max_length=100)
    cat_info=models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return self.cat_name
class Sub_Category(Base_Model):
    sub_cat_name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_cat_name

class Market(Base_Model):
    market_name=models.CharField(max_length=200)
    market_info = models.CharField(max_length=100, blank=True, null=True)
    rating=models.FloatField(default=0.0)

    def __str__(self):
        return self.market_name


class Product(Base_Model):
    pro_name=models.CharField(max_length=255)
    sub_category=models.ForeignKey(to=Sub_Category, related_name="product_sub_cat", on_delete=models.CASCADE)
    market=models.ForeignKey(to=Market,on_delete=models.CASCADE)
    product_info=models.TextField(blank=True, null=True)
    rating=models.FloatField(default=0.0)
    product_usage=models.TextField( blank=True, null=True)
    price=models.IntegerField(default=0)

    def get_product_sizes(self):
        sizes=Size.objects.filter(sub_cat=self.sub_category)
        return sizes







    def __str__(self):
        return self.pro_name

class Images(Base_Model):
    img_file=models.ImageField(upload_to='images/')
    product=models.ForeignKey(Product, related_name='product_images',on_delete=models.CASCADE)




class Comment(Base_Model):
    comment_text=models.TextField()
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)



    def __str__(self):
        return self.comment_text[:10]

class Order_one(Base_Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    count =models.IntegerField(default=1)
    is_ordered = models.BooleanField(default=False)


    def __str__(self):
        return self.product.pro_name



class Order(Base_Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_one=models.ManyToManyField(Order_one)

    is_ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.order_one.first().product.pro_name








