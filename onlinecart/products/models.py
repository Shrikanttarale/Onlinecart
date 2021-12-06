from django.db import models
from django.conf import settings


QUANTITY_TYPE=(
    ('250gm','250 Grams'),
    ('500gm','500 Grams'),
    ('1000gm','1000 Grams'),
    ('2000gm','2000 Grams'),
    ('3000gm','3000 Grams'),
    ('1PC', '1 Pc'),
    ('12PC', '12 Pc')
)
PRODUCT_TYPE=(
    ('V','Vegitables'),
    ('F','Fruits')
)
# Create your models here.
class Products(models.Model):
    product_name=models.CharField(blank=False,null=False,max_length=20)
    product_desc=models.TextField(max_length=500,blank=True)
    product_price=models.FloatField(default=0.0)
    product_dis_price=models.FloatField(null=True,blank=True)
    product_qty_type=models.CharField(choices=QUANTITY_TYPE,max_length=12)
    product_qty=models.IntegerField(blank=False,null=False)
    product_type=models.CharField(choices=PRODUCT_TYPE,max_length=1)
    product_photo=models.ImageField(upload_to='products/',blank=False,null=False)

    def __str__(self):
        return self.product_name


class Wishlist(models.Model):
    wishlist_user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    wishlist_product=models.ForeignKey(Products,on_delete=models.CASCADE)
    wishlist_created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wishlist_product.product_name

