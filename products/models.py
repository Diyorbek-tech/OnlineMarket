from accounts.models import  User
from django.db import models
from base.BaseModel import Base_Model

from django.template.defaultfilters import slugify

from payments.models import Payment,Coupon,Split_the_bill

class Size(Base_Model):
    sub_cat=models.ForeignKey("Sub_Category",on_delete=models.CASCADE)
    size=models.CharField(max_length=15)

    def __str__(self):
        return f"{self.sub_cat.sub_cat_name} of {self.size}"
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
    PRODUCT_STATUS=(
        ("Eng zo`r narx","Eng zo`r narx"),
        ("Ko`p sotilgan","Ko`p sotilgan"),
        ("Yangi kelgan","Yangi kelgan"),
        ("Ajoyib taklif","Ajoyib taklif"),
        ("Ekskluziv taklif","Ekskluziv taklif"),
    )
    pro_name=models.CharField(max_length=255)
    sub_category=models.ForeignKey(to=Sub_Category, related_name="product_sub_cat", on_delete=models.CASCADE)
    market=models.ForeignKey(to=Market,on_delete=models.CASCADE)
    product_info=models.TextField(blank=True, null=True)
    rating=models.FloatField(default=0.0)
    product_usage=models.TextField( blank=True, null=True)
    price=models.IntegerField(default=0)
    slug=models.SlugField(blank=True,null=True,unique=True)
    discount=models.IntegerField(default=0,blank=True,null=True)
    product_status=models.CharField(max_length=20,choices=PRODUCT_STATUS,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.pro_name)
        return super().save(*args,**kwargs)

    def get_product_sizes(self):
        sizes=Size.objects.filter(sub_cat=self.sub_category)
        return sizes

    def __str__(self):
        return self.pro_name

    class Meta:
        ordering='-created_date',
        get_latest_by="created_date"
        # db_table
        # abstract=True
        verbose_name="sadasf"
        verbose_name_plural='Product-s'
        required_db_vendor="mysql",""



class Images(Base_Model):
    img_file=models.ImageField(upload_to='images/')
    product=models.ForeignKey(Product, related_name='product_images',on_delete=models.CASCADE)
class Message(Base_Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    message_text = models.TextField()
    comment=models.ForeignKey("Comment",on_delete=models.CASCADE)
    is_reply = models.BooleanField(default=False)
    like = models.IntegerField()
    review = models.IntegerField()


    def __str__(self):
        return self.message_text[:10]



class Comment(Base_Model):
    pass

#
#
# class Reply(Base_Model):
#     message = models.ManyToManyField(Message)





class Order_one(Base_Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    count =models.IntegerField(default=1)
    is_ordered = models.BooleanField(default=False)


    def get_absolute_price(self):
        if self.product.discount:
            return self.product.price-self.product.discount
        else:
            return self.product.price
    def get_order_one_price(self):
        return self.get_absolute_price() * self.count



    def __str__(self):
        return self.product.pro_name
class Order(Base_Model):
    MONTHS=(
        ("3","3"),
        ("6","6"),
        ("12","12"),
        ("18","18"),
        ("24","24"),
    )


    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order_one=models.ManyToManyField(Order_one)

    shipping_address=models.ForeignKey("Address",on_delete=models.RESTRICT,related_name="shipping_order",blank=True,null=True)
    billing_address=models.ForeignKey("Address",on_delete=models.RESTRICT,related_name="billing_order",blank=True,null=True)

    payment=models.ForeignKey(to=Payment,on_delete=models.RESTRICT,blank=True,null=True)
    coupon=models.ForeignKey(to=Coupon,on_delete=models.RESTRICT,blank=True,null=True)

    splittheprice=models.CharField(max_length=4,choices=MONTHS,default=MONTHS[0][1],blank=True,null=True)


    on_rode=models.BooleanField(default=False)
    delivered=models.BooleanField(default=False)
    received=models.BooleanField(default=False)

    is_ordered=models.BooleanField(default=False)

    def get_order_price(self):
        total=0
        for i in self.order_one.all():
            total+=i.get_order_one_price()
        return total

    def get_order_total_with_cp(self):
        return self.get_order_price()-self.coupon.amount
    def get_split_price(self,month,gavep=None):
        if gavep:
            return Split_the_bill(self.get_order_price() - self.coupon.amount, month,gavep)
        else:
            return Split_the_bill(self.get_order_price() - self.coupon.amount, month)


    def __str__(self):
        return self.order_one.first().product.pro_name
class Address(Base_Model):
    ADDRESS_TYPE=(
       ('SHIPPING','SHIPPING'),
       ('BILLING','BILLING'),
    )

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    street=models.CharField(max_length=100)
    house=models.CharField(max_length=100)
    zip_code=models.IntegerField()

    address_type=models.CharField(choices=ADDRESS_TYPE,max_length=30)










