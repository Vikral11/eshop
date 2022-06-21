from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register((contactus,newsletter,main_cat,sub_cat,brand,seller,buyer,product,wishlist, checkout, checkoutproducts))
 