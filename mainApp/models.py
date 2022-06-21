from django.db import models

# Create your models here.
class main_cat(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class sub_cat(models.Model):
    name= models.CharField(max_length=20)
    def __str__(self):
        return self.name

class brand(models.Model):
    name= models.CharField(max_length=20)

    def __str__(self):
        return self.name

class seller(models.Model):
    name= models.CharField(max_length=20)
    user_name= models.CharField(max_length=20)
    email= models.EmailField(max_length=20,unique=True)
    phone= models.CharField(max_length=12)
    address1= models.TextField(max_length=100,default=None ,blank=True, null=True)
    address2= models.TextField(max_length=100,default=None ,blank=True, null=True)
    address3= models.TextField(max_length=100,default=None ,blank=True, null=True)
    pin=models.CharField(max_length=10,default=None ,blank=True, null=True)
    city= models.CharField(max_length=20,default=None ,blank=True, null=True)
    state= models.CharField(max_length=20,default=None ,blank=True, null=True)
    pic=models.ImageField(upload_to="images/", default=None ,blank=True, null=True)
    def __str__(self):
        return self.name


class buyer(models.Model):
    name= models.CharField(max_length=20)
    user_name= models.CharField(max_length=20)
    email= models.EmailField(max_length=20, unique=True)
    phone= models.CharField(max_length=12)
    address1= models.TextField(max_length=100,default=None ,blank=True, null=True)
    address2= models.TextField(max_length=100,default=None ,blank=True, null=True)
    address3= models.TextField(max_length=100,default=None ,blank=True, null=True)
    pin=models.CharField(max_length=10,default=None ,blank=True, null=True)
    city= models.CharField(max_length=20,default=None ,blank=True, null=True)
    state= models.CharField(max_length=20,default=None ,blank=True, null=True)
    def __str__(self):
        return self.name
    
class product(models.Model):
      name= models.CharField(max_length=30)
      main_cat=models.ForeignKey(main_cat, on_delete= models.CASCADE)
      main_cat1=models.CharField(max_length=30,blank=True, null=True)    
      sub_cat=models.ForeignKey(sub_cat, on_delete= models.CASCADE)
      sub_cat1=models.CharField(max_length=30,blank=True, null=True)
      brand=models.ForeignKey(brand, on_delete= models.CASCADE)
      brand1=models.CharField(max_length=30,blank=True, null=True)
      seller=models.ForeignKey(seller, on_delete= models.CASCADE)
      seller1=models.CharField(max_length=30,blank=True, null=True)
      baseprice=models.IntegerField()
      discount=models.IntegerField()
      final_price=models.IntegerField()
      color= models.CharField(max_length=20)
      size=  models.CharField(max_length=20)
      desc= models.TextField()
      stock= models.CharField(max_length=20)
      date= models.DateTimeField(auto_now=True)
      pic1=models.ImageField(upload_to="media/productimages/",default=None ,blank=True, null=True)
      pic2=models.ImageField(upload_to="media/productimages/",default=None ,blank=True, null=True)
      pic3=models.ImageField(upload_to="media/productimages/",default=None ,blank=True, null=True)
      pic4=models.ImageField(upload_to="media/productimages/",default=None ,blank=True, null=True)
      def __str__(self):
        return self.name


class wishlist(models.Model):
    name= models.ForeignKey(buyer , on_delete= models.CASCADE)
    products= models.ForeignKey(product,on_delete= models.CASCADE)


    def __str__(self):
        return str(self.id)+" "+str(self.name.name)+" "+str(self.products.name)



class newsletter(models.Model):

    mail=models.CharField(max_length=30)
    def __str__(self):
        return self.mail


choice=((1,"Not Packed"),(2,"Packed"),(3,"Out For Delivery"),(4,"Delivered"))
paymentstat=((1, "Pending"), (2, "Done"))

class checkout(models.Model):
    buyer= models.ForeignKey(buyer, on_delete=models.CASCADE)
    total= models.IntegerField(default=0, null=True, blank=True)
    shipping= models.IntegerField(default=0, null=True, blank=True)
    final= models.IntegerField(default=0, null=True, blank=True)
    mode=models.CharField(max_length=20, null=True, blank=True)
    paymentstatus=models.IntegerField(choices=paymentstat,default=1)
    active=models.BooleanField(default=True)
    
    date= models.DateTimeField(auto_now=True)
    rppid=models.CharField(max_length=50, null=True, blank=True)
    rpoid=models.CharField(max_length=50, null=True, blank=True)
    rpsid=models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return str(self.id)+" "+ self.buyer.name





class checkoutproducts(models.Model):
    product= models.ForeignKey(product, on_delete=models.CASCADE)
    qty= models.IntegerField(default=1)
    total=models.IntegerField(default=0)
    checkout= models.ForeignKey(checkout, on_delete=models.CASCADE)
    seller=models.ForeignKey(seller, on_delete=models.CASCADE)
    active=models.BooleanField(default=True)
    orderstatus=models.IntegerField(choices=choice,default=1)
    buyer= models.ForeignKey(buyer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.checkout.id)+" "+ self.product.name



class contactus(models.Model):
    name= models.CharField(max_length=20)
    email= models.EmailField(max_length=20)
    phone= models.IntegerField()
    subject= models.CharField(max_length=80)
    desc=  models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)+self.name



