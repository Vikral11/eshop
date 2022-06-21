from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
import os
from django.contrib.auth.decorators import login_required
import razorpay
from eshop.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
from django.db.models import Q
from random import randint
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
@csrf_exempt
def home(request):
    try:
        user= User.objects.get(username=request.user)
        if (user.is_superuser):
            return HttpResponseRedirect("/admin")
    except:
        pass
    p= product.objects.all()
    p= p[::-1]
    
            
    return render(request, "index.html", {"products": p})

def login(request):
    if(request.method=="POST"):
            username= request.POST.get("name")
            password= request.POST.get("password")
            user= auth.authenticate(username=username, password=password)
            if(user is not None):
                auth.login(request, user)
                return HttpResponseRedirect("/") 

            else:
                messages.error(request, "username password dont match")
    
    return render(request, "login.html")

def about(request):

    
    return render(request, "about.html")




def signup(request):
    
    if (request.method=="POST"):
        type = request.POST.get("actype")
        if(type=="seller"):
            try:
                buy=buyer.objects.get(email=request.POST.get("email"))
                print("hiiiiiiiiiiiiiiii")
                messages.error(request,"Email is already registered")
            except:
                try:
                    s= seller()
                    s.name= request.POST.get("fname")
                    s.user_name= request.POST.get("name")
                    s.email= request.POST.get("email")
                    
                    s.phone= request.POST.get("phone")
                    s.user_name= request.POST.get("name")
                    password= request.POST.get("password")
                    cpassword= request.POST.get("cpassword")
                    if(password==cpassword):
                        try:
                        
                            user = User.objects.create_user(username= s.user_name, password= password, email= s.email)   
                            user.save()
                            s.save()
                            return HttpResponseRedirect("/login")

                        except:
                            messages.error(request,"Username already exist")
                    else:
                        messages.error(request,"Password and Confirm Password Does not Match")
                except:
                    messages.error(request,"Email is already registered")

        else:
            try:
                sel=seller.objects.get(email=request.POST.get("email"))
                messages.error(request,"Email is already registered")
            except:
                try:
                    b= buyer()
                    b.name= request.POST.get("fname")
                    b.user_name= request.POST.get("name")
                    b.email= request.POST.get("email")
                    b.phone= request.POST.get("phone")
                    b.user_name= request.POST.get("name")
                    password= request.POST.get("password")
                    cpassword= request.POST.get("cpassword")
                    if(password==cpassword):
                        try:
                        
                            user = User.objects.create_user(username= b.user_name, password= password, email= b.email)   
                            user.save()
                            b.save()
                            return HttpResponseRedirect("/login")

                        except:
                            messages.error(request,"Username already exist")




                    else:
                        messages.error(request,"Password and Confirm Password Does not Match")

                except:
                    messages.error(request,"Email is already registered")

    return render(request, "signup.html")


@login_required(login_url= "/login/")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")


@login_required(login_url= "/login/")
def profile(request):
    try:
        user= User.objects.get(username=request.user)
        if (user.is_superuser):
            return HttpResponseRedirect("/admin")

        else:
            Seller= seller.objects.get(user_name=request.user)
            p= product.objects.filter(seller=Seller)
            p= p[::-1]
            return render(request, "sellerprofile.html", {"seller": Seller, "products":p})

       


    except:
        Buyer= buyer.objects.get(user_name=request.user)
        check= checkout.objects.filter(buyer= Buyer)
 
        
        w= wishlist.objects.filter(name= Buyer)
        
        
        
        return render(request, "buyerprofile.html" , {"buyer":Buyer, "wishlist":w, "Check":check})

@login_required(login_url= "/login/")  
def updateseller(request):
    
        
    Seller= seller.objects.get(user_name=request.user)
    if (request.method=="POST"):
        if(request.FILES.get("pic")):
            picname=str(Seller.pic)
            Seller.pic= request.FILES.get("pic")
            if(picname):
                try:
                    os.remove("media/"+picname)
                except:
                    pass
            

        Seller.name= request.POST.get("fname")
        Seller.email= request.POST.get("email")
        Seller.phone= request.POST.get("phone")
        Seller.address1= request.POST.get("add1")
        Seller.address2= request.POST.get("add2")
        Seller.address3= request.POST.get("add3")
        Seller.pin= request.POST.get("pin")
        Seller.city= request.POST.get("city")
        Seller.state= request.POST.get("state")
        
        Seller.save()
        return HttpResponseRedirect("/profile")
        

    return render(request, "updateseller.html" , {"seller": Seller})

@login_required(login_url= "/login/")
def addproducts(request):
    main= main_cat.objects.all()
    sub= sub_cat.objects.all()
    bran= brand.objects.all()


    if(request.method=="POST"):
        s= seller.objects.get(user_name=request.user)
        p=product()
        p.name=request.POST.get("pname")
        p.main_cat= main_cat.objects.get(name=request.POST.get('maincat'))
        p.main_cat1= request.POST.get('maincat')
        p.sub_cat= sub_cat.objects.get(name=request.POST.get("subcat"))
        p.sub_cat1= request.POST.get("subcat")
        p.brand= brand.objects.get(name=request.POST.get("brand"))
        p.brand1= request.POST.get("brand")
        p.stock=request.POST.get("stock")
        p.baseprice=int(request.POST.get("bp"))
        p.discount=int(request.POST.get("dp"))
        p.final_price=p.baseprice- p.baseprice*p.discount/100

        p.color=request.POST.get("colour")
        p.size=request.POST.get("size")
        p.desc=request.POST.get("desc")
        p.pic1=request.FILES.get("pic1")
        p.pic2=request.FILES.get("pic2")
        p.pic3=request.FILES.get("pic3")
        p.pic4=request.FILES.get("pic4")
        p.seller= s
        p.seller1= s.name
        p.save()
        HttpResponseRedirect("/profile")
        


        



    return render(request, "addproducts.html" ,{"Main": main, "Sub":sub, "Brand":bran} )




@login_required(login_url= "/login/")
def delpro(request, id):
    Seller= seller.objects.get(user_name=request.user)
    p= product.objects.get(id=id)
    
    
    if(p.seller==Seller):
        p.delete()
    return HttpResponseRedirect("/profile")

@login_required(login_url= "/login/")
def updpro(request,id):
    Seller= seller.objects.get(user_name=request.user)
    p= product.objects.get(id=id)
    main= main_cat.objects.exclude(name=p.main_cat)
    sub= sub_cat.objects.exclude(name=p.sub_cat)
    bran= brand.objects.exclude(name=p.brand)


    
    if(request.method=="POST"):
        Seller= seller.objects.get(user_name=request.user)
        if(p.seller==Seller):
            p.seller1= Seller.name
            p.name=request.POST.get("pname")
            p.main_cat= main_cat.objects.get(name=request.POST.get('maincat'))
            p.main_cat1= request.POST.get('maincat')
            p.sub_cat= sub_cat.objects.get(name=request.POST.get("subcat"))
            p.sub_cat1= request.POST.get("subcat")
            p.brand= brand.objects.get(name=request.POST.get("brand"))
            p.brand1= request.POST.get("brand")
            p.stock=request.POST.get("stock")
            p.baseprice=int(request.POST.get("bp"))
            p.discount=int(request.POST.get("dp"))
            p.final_price=p.baseprice- p.baseprice*p.discount/100

            p.color=request.POST.get("colour")
            p.size=request.POST.get("size")
            p.desc=request.POST.get("desc")
            if(request.FILES.get("pic1")):
                picname= str(p.pic1)
                p.pic1=request.FILES.get("pic1")
                if(picname):
                    try:
                        os.remove("media/"+picname)
                    except:
                        pass
            if(request.FILES.get("pic2")):
                picname= p.pic2
                p.pic2=request.FILES.get("pic2")
                if(picname):
                    try:
                        os.remove("media/"+picname)
                    except:
                        pass
            if(request.FILES.get("pic3")):
                picname= p.pic3
                p.pic3=request.FILES.get("pic3")
                if(picname):
                    try:
                        os.remove("media/"+picname)
                    except:
                        pass
            if(request.FILES.get("pic4")):
                picname= p.pic4
                p.pic4=request.FILES.get("pic4")
                if(picname):
                    try:
                        os.remove("media/"+picname)
                    except:
                        pass


            
            
            
            p.save()
            return HttpResponseRedirect("/profile")

        else:
            return HttpResponseRedirect("/profile")

        



    return render(request, "updatepro.html", {"product":p,"Main": main, "Sub":sub, "Brand":bran} )









@csrf_exempt
def shop(request,mains, sub, bran,fil):
    if(request.method=="POST"):
        Search= request.POST.get("search")
        
        pro= product.objects.filter((Q(brand1__icontains=Search) | Q(name__icontains=Search) 
        | Q(main_cat1__icontains=Search) | Q(sub_cat1__icontains=Search) | Q(color__icontains=Search) | Q(size__icontains=Search) | Q(desc__icontains=Search))).order_by("date")
        mcat=main_cat.objects.all()
        scat=sub_cat.objects.all()
        brans=brand.objects.all()
        pro= pro[::-1]
        
        
        
        return render(request,"shop.html" , {"Maincat":mcat , "Subcat":scat , "Brand": brans, "products":pro, "Sub":sub,"Bran":bran,"Main":mains, "search":Search})


    else:
        if(mains=="All" and  sub=="All"and bran=="All"):
            if (fil=="date"):
                pro= product.objects.all().order_by("date")
                pro= pro[::-1]
            elif (fil=="name"):
                pro= product.objects.all().order_by("name")
                
            elif (fil=="price1"):
                pro= product.objects.all().order_by("final_price")
                
                
            elif (fil=="price2"):
                pro= product.objects.all().order_by("final_price")
                pro= pro[::-1]
                
            
                
        elif(mains!="All"and sub=="All"and bran=="All"):
            if (fil=="date"):
                pro= product.objects.filter(main_cat= main_cat.objects.get(name=mains)).order_by("date")
                pro= pro[::-1]
            elif (fil=="name"):
                pro= product.objects.filter(main_cat= main_cat.objects.get(name=mains)).order_by("name")
            elif (fil=="price1"):
                pro= product.objects.filter(main_cat= main_cat.objects.get(name=mains)).order_by("final_price")
                
                
            elif (fil=="price2"):
                pro= product.objects.filter(main_cat= main_cat.objects.get(name=mains)).order_by("final_price")
                pro= pro[::-1]
            
        elif(mains=="All" and sub!="All"and bran=="All"):
            
            if (fil=="date"):
                pro= product.objects.filter(sub_cat= sub_cat.objects.get(name=sub)).order_by("date")
                pro= pro[::-1]
            elif (fil=="name"):
                pro= product.objects.filter(sub_cat= sub_cat.objects.get(name=sub)).order_by("name")
            elif (fil=="price1"):
                pro= product.objects.filter(sub_cat= sub_cat.objects.get(name=sub)).order_by("final_price")
                
                
            elif (fil=="price2"):
                pro= product.objects.filter(sub_cat= sub_cat.objects.get(name=sub)).order_by("final_price")
                pro= pro[::-1]
        elif(mains=="All"and sub=="All"and bran!="All"):
            
            if (fil=="date"):
                pro= product.objects.filter(brand=brand.objects.get(name=bran)).order_by("date")
                pro= pro[::-1]
            elif (fil=="name"):
                pro= product.objects.filter(brand=brand.objects.get(name=bran)).order_by("name")
            elif (fil=="price1"):
                pro= product.objects.filter(brand=brand.objects.get(name=bran)).order_by("final_price")
                
                
            elif (fil=="price2"):
                pro= product.objects.filter(brand=brand.objects.get(name=bran)).order_by("final_price")
                pro= pro[::-1]

        elif(mains!="All"and sub!="All" and bran=="All"):
            if (fil=="date"):
                pro= product.objects.filter(main_cat= main_cat.objects.get(name=mains),sub_cat= sub_cat.objects.get(name=sub)).order_by("date")
                pro= pro[::-1]
            elif (fil=="name"):
                pro= product.objects.filter(main_cat= main_cat.objects.get(name=mains),sub_cat= sub_cat.objects.get(name=sub)).order_by("name")
            elif (fil=="price1"):
                pro= product.objects.filter(main_cat= main_cat.objects.get(name=mains),sub_cat= sub_cat.objects.get(name=sub)).order_by("final_price")
                
                
            elif (fil=="price2"):
                pro= product.objects.filter(main_cat= main_cat.objects.get(name=mains),sub_cat= sub_cat.objects.get(name=sub)).order_by("final_price")
                pro= pro[::-1]
            
        
        elif(mains=="All"and sub!="All" and bran!="All"):
            if (fil=="date"):
                pro= product.objects.filter(brand=brand.objects.get(name=bran),sub_cat= sub_cat.objects.get(name=sub)).order_by("date")
                pro= pro[::-1]
            elif (fil=="name"):
                pro= product.objects.filter(brand=brand.objects.get(name=bran),sub_cat= sub_cat.objects.get(name=sub)).order_by("name")
            elif (fil=="price1"):
                pro= product.objects.filter(brand=brand.objects.get(name=bran),sub_cat= sub_cat.objects.get(name=sub)).order_by("final_price")
                
                
            elif (fil=="price2"):
                pro= product.objects.filter(brand=brand.objects.get(name=bran),sub_cat= sub_cat.objects.get(name=sub)).order_by("final_price")
                pro= pro[::-1]
            

        elif(mains!="All"and sub=="All" and bran!="All"):
            if (fil=="date"):
                pro= product.objects.filter(brand=brand.objects.get(name=bran),main_cat= main_cat.objects.get(name=mains)).order_by("date")
                pro= pro[::-1]
            elif (fil=="name"):
                pro= product.objects.filter(brand=brand.objects.get(name=bran),main_cat= main_cat.objects.get(name=mains)).order_by("name")
            elif (fil=="price1"):
                pro= product.objects.filter(brand=brand.objects.get(name=bran),main_cat= main_cat.objects.get(name=mains)).order_by("final_price")
                
                
            elif (fil=="price2"):
                pro= product.objects.filter(brand=brand.objects.get(name=bran),main_cat= main_cat.objects.get(name=mains)).order_by("final_price")
                pro= pro[::-1]
            
        elif(mains!="All"and sub!="All" and bran!="All"):
            if (fil=="date"):
                pro= product.objects.all().order_by("date")
                pro= pro[::-1]
            elif (fil=="name"):
                pro= product.objects.all().order_by("name")
            elif (fil=="price1"):
                pro= product.objects.all().order_by("final_price")
                
                
            elif (fil=="price2"):
                pro= product.objects.filter(brand=brand.objects.get(name=bran),main_cat= main_cat.objects.get(name=mains),sub_cat= sub_cat.objects.get(name=sub)).order_by("final_price")
            

        


  


        mcat=main_cat.objects.all()
        scat=sub_cat.objects.all()
        brans=brand.objects.all()
        
        
        
        return render(request,"shop.html" , {"Maincat":mcat , "Subcat":scat , "Brand": brans, "products":pro, "Sub":sub,"Bran":bran,"Main":mains})




def productp(request,id):
    pro= product.objects.get(id=id)
    return render(request, "productp.html",{"product":pro})


@login_required(login_url= "/login/")
def updatebuyer(request):
    Buyer= buyer.objects.get(user_name= request.user)
    if(request.method=="POST"):
        Buyer.name= request.POST.get("fname")
        Buyer.email= request.POST.get("email")
        Buyer.phone= request.POST.get("phone")
        Buyer.address1= request.POST.get("add1")
        Buyer.address2= request.POST.get("add2")
        Buyer.address3= request.POST.get("add3")
        Buyer.pin= request.POST.get("pin")
        Buyer.city= request.POST.get("city")
        Buyer.state= request.POST.get("state")
        
        Buyer.save()
        return HttpResponseRedirect("/profile")

    return render (request,"updatebuyer.html", {"buyer":Buyer})


@login_required(login_url= "/login/")
def wishlistt(request, id):
    try:
   
        user= buyer.objects.get(user_name= request.user)
        prod= product.objects.get(id=id)
        wish= wishlist.objects.filter(name= user)
        
        flag= False
        for i in wish:
            if(id== i.products.id):
                flag= True
                break
        
        if(flag==False):
            w= wishlist()
            w.name= user
            w.products= prod
            w.save()
        return HttpResponseRedirect("/profile/")
    except:
        return render (request,"accessdenied.html")
@login_required(login_url= "/login/")
def removeproduct(request,id):
    Buyer=buyer.objects.get(user_name=request.user)
    w=wishlist.objects.get(id=id)
    if(w.name==Buyer):
        w.delete()

    return HttpResponseRedirect("/profile/")



@login_required(login_url= "/login/")

def AddToCart(request, id):
    cart= request.session.get("cart", None)
    if(cart):
        if(str(id) in cart):
            q= cart[str(id)]
            cart[str(id)]= q+1
        else:
            cart.setdefault(str(id), 1)

    else:
        cart= {str(id):1}
    request.session["cart"]=cart
    request.session.set_expiry(60*60*24*30)
    print(cart)
    return HttpResponseRedirect("/cart")


@login_required(login_url= "/login/")
def cart(request):
    if(request.method=="POST"):
        return HttpResponseRedirect("/checkout")
    cart= request.session.get("cart", None)
    total=0
    shipping=0
    final=0
    products=[]
    if(cart):
        for keys, values in cart.items():
            p= product.objects.get(id=keys)
            products.append(p)
            total= total+p.final_price*values
    if(total<500 and len(products)>0):
        shipping=100

    final= total+shipping
    

    

    
    
    
    
    

    return render(request, "cart.html",{"product":products,
                                        "Total":total,
                                        "Shipping":shipping,
                                        "Final": final })



@login_required(login_url= "/login/")
def rcart(request, id):
    cart= request.session.get("cart",None)
    try:
        if (cart):
            cart.pop(str(id))
            request.session["cart"]=cart
        return HttpResponseRedirect("/cart")
    except:
        return HttpResponseRedirect("/profile")


@login_required(login_url= "/login/")
def ucart(request, id, num):
    cart= request.session.get("cart", None)
    try:   
        if(cart):
            qty= cart[str(id)]
            if(num==0):
                cart[str(id)]= qty+1
            elif(num==1 and qty>1):
                cart[str(id)]= qty-1

            elif(num==1 and qty==1):
                print("pop")
                cart.pop(str(id))
            request.session["cart"]=cart


            return HttpResponseRedirect("/cart")
    except:
        return HttpResponseRedirect("/profile")



@login_required(login_url= "/login/")
def orderplaced(request):
    return render(request, "orderplaced.html")


        
        

client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
@login_required(login_url= "/login/")
def checkouts(request):
    try:
        b= buyer.objects.get(user_name=request.user)
        cart=request.session.get("cart",None)
        products=[]
        total=0
        final=0
        shipping=0
        if (cart):
            for keys in cart.keys():
                p=product.objects.get(id=keys)
                products.append(p)
                total=total+p.final_price*cart[keys]
            
            if (total<500 and len(products)>0):
                shipping=100
            
            final=total+shipping



            if (request.method=="POST"):
                Mode= request.POST.get("mode")
                Buyer= buyer.objects.get(user_name= request.user) 
                
                if(Mode=="COD"):
                    c= checkout()
                    c.buyer=Buyer
                    c.total=total
                    c.shipping=shipping
                    c.final=final
                    c.mode="COD"
                    c.paymentstatus=1
                    c.save()
                    for key in cart.keys():
                        p= product.objects.get(id=key)
                        cp= checkoutproducts()
                        cp.buyer=Buyer
                        cp.seller= p.seller
                        cp.active= True
                        cp.orderstatus= 1
                        cp.product=product.objects.get(id=key)
                        cp.qty= cart[key]
                        cp.total=p.final_price*cart[key]
                        cp.checkout=c
                        cp.save()
                        
                    return HttpResponseRedirect("/orderplaced")
            
                elif (Mode=="Net"):
                    c= checkout()
                    c.buyer=Buyer
                    c.total=total
                    c.shipping=shipping
                    c.final=final
                    c.mode="Net Banking"
                    c.save()
                    for key in cart.keys():
                        p= product.objects.get(id=key)
                        cp= checkoutproducts()
                        cp.buyer=Buyer
                        cp.seller= p.seller
                        cp.product=product.objects.get(id=key)
                        cp.qty= cart[key]
                        cp.total=p.final_price*cart[key]
                        cp.checkout=c
                        cp.save()

                    orderAmount = c.final*100
                    orderCurrency = "INR"
                    paymentOrder = client.order.create(dict(amount=orderAmount,currency=orderCurrency,payment_capture=1))
                    paymentId = paymentOrder['id']
                    
                    c.save()
                    return render(request,"pay.html",{
                        "amount":orderAmount,
                        "api_key":RAZORPAY_API_KEY,
                        "order_id":paymentId,
                        "User":Buyer, "Checkout":str(c.id)})
                    

                
        
        
        return render (request, "checkout.html", {"buyer":b,"product":products, "Total":total,
                                            "Shipping":shipping,
                                            "Final": final})

    except:
        return render(request,"accessdenied.html")


@login_required(login_url= "/login/")
def paynow(request, id):
    try:
        Buyer= buyer.objects.get(user_name=request.user)
    except:
        HttpResponseRedirect("/profile/")


    c= checkout.objects.get(id=id)
    orderAmount = c.final*100
    orderCurrency = "INR"
    paymentOrder = client.order.create(dict(amount=orderAmount,currency=orderCurrency,payment_capture=1))
    paymentId = paymentOrder['id']
    
    c.save()
    print("helllloooooooooo")
    return render(request,"pay.html",{
        "amount":orderAmount,
        "api_key":RAZORPAY_API_KEY,
        "order_id":paymentId,
        "User":Buyer, "Checkout":str(c.id),
       })


@login_required(login_url= "/login/")
def paymentsuccess(request, rppid, rpoid, rpsid,chid):
    
    buyer = buyer.objects.get(user_name=request.user)
    Check = checkout.objects.get(id= int(chid))
    Check.mode="Net Banking"
    Check.rppid=rppid
    Check.rpoid=rpoid
    Check.rpsid=rpsid
    Check.paymentstatus=2
    Check.save()
    return HttpResponseRedirect('/orderplaced')



def contact(request):
    if(request.method=="POST"):
        c=contactus()
        c.name=request.POST.get("name")
        c.email=request.POST.get("mail")
        c.phone=request.POST.get("phone")
        c.subject=request.POST.get("subject")
        c.desc=request.POST.get("desc")
        c.save()

        subject = 'We are looking into your concern'
        message ="""We have recieved your concern, it will get resolved within next 48hrs.
For further queries please contact the customer care.
Thankyou
Team: Eshop"""
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [c.email] 
        send_mail( subject, message, email_from, recipient_list )

    return render(request, "contact.html")

def Newsletter(request):
    if(request.method=="POST"):
        flag=False
        news= newsletter.objects.all()
        emailid= request.POST.get("emailid")
        for i in news:
            if(emailid== i.mail):
                flag=True
                break
        if(flag== False):
            new= newsletter()
            new.mail= request.POST.get("emailid")
            new.save()
            subject = 'Thanks for Subscribing'
            message = """Welcome to Eshop family.
Thanks for subscribing to our newsletter service, Now you will get early updates about our new products and offers.
Team: Eshop"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [new.mail] 
            send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect("/")





def forgetpass_email(request):
    if(request.method=="POST"):
        mail= request.POST.get("mail")
        act= request.POST.get("actype")
        if(act=="buyer"):
            try:
                user= buyer.objects.get(email=mail)
                otp= randint(100000,999999)
                request.session["User"]= mail
                request.session["num"]= otp
                subject = 'Password reset'
                message = """your OTP is %d
                        Team: Eshop"""%otp
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [mail] 
                send_mail( subject, message, email_from, recipient_list )

                

                


            except:
                messages.error(request,"Please Enter Registered Email")
        elif(act=="seller"):
            try:
                user= seller.objects.get(email=mail)
                otp= randint(100000,999999)
                request.session["User"]= mail
                request.session["num"]= otp
                subject = 'Password reset'
                message = """your OTP is %d
                        Team: Eshop"""%otp
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [mail] 
                send_mail( subject, message, email_from, recipient_list )

                

                


            except:
                messages.error(request,"Please Enter Registered Email")
        print("hello")
        return HttpResponseRedirect("/forgetpass_otp")
        print("hiiii")
    return render (request, "forgetpass_email.html")













def forgetpass_otp(request):
    if(request.method=="POST"):
        otp= int(request.POST.get("OTP"))
        num= int(request.session.get("num"))
        if(num==otp):
            return HttpResponseRedirect("/forgetpass_newpass")

    return render(request , "forgetpass_otp.html")

def forgetpass_newpass(request):
    if(request.method=="POST"):
        passw= request.POST.get("pass")
        cpassw= request.POST.get("cpass")
        if(passw==cpassw):
            print(request.session.get('User'))
            user= User.objects.get(email= request.session.get('User'))
            user.set_password(passw)
            user.save()
            return HttpResponseRedirect("/login/")
            
        else:
            messages.error(request,"Password and Confirm Password dont match")
    return render(request , "forgetpass_newpass.html")
    

def sellerorders(request):
    sell= seller.objects.get(user_name= request.user)
    pro= checkoutproducts.objects.filter(seller=sell)
    return render(request,"sellerorders.html", {"products": pro,})  


def updateorderhistory(request,id):
    checkouts= checkoutproducts.objects.get(id=id)
    if (request.method=="POST"):
        print(request.POST.get("paymentstat"), type(request.POST.get("paymentstat")))
        checkouts.orderstatus=request.POST.get("orderstat")
        checkouts.active=request.POST.get("actistat")
        checkouts.checkout.paymentstatus=str(1)
        checkouts.checkout.save()
        checkouts.save()
        return HttpResponseRedirect("/orderhistory/")

    return render (request,"updateorders.html",{"i":checkouts})


