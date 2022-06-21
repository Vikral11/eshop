from django import template
register= template.Library()
from ..models import *



@register.filter(name="cartqty")
def cartQty(request,num):
    cart= request.session.get("cart",None)
    if(cart):
        return cart[str(num)]
    else:
        return None




@register.filter(name="cartTotal")
def cartTotal(request,num):
    cart= request.session.get("cart",None)
    p= product.objects.get(id=num)
    if(cart):
        return (cart[str(num)]*p.final_price)
    else:
        return None



@register.filter(name="checkshow")
def checkShow(request, Final):
    if (Final>0):
        return 1

    else:
        return 0


@register.filter(name="checkproduct")
def checkproduct(request, id):
    check= checkout.objects.get(id=id)
    checkp= checkoutproducts.objects.filter(checkout=check)
    return checkp




@register.filter(name="orderstat")
def orderstat(request, i):
    if(i.orderstatus==1):
        return "Not Packed"
    elif(i.orderstatus==2):
        return "Packed"

    elif(i.orderstatus==3):
        return "Out For Delivery"
    elif(i.orderstatus==4):
        return "Delivered"


@register.filter(name="paystat")
def paymentstat(request, i):
    if(i.paymentstatus==1):
        return "Pending"
    elif(i.paymentstatus==2):
        return "Done"




@register.filter(name="paynow")
def paynow(request, i):

    print(i.paymentstatus , i.mode)
    if(i.paymentstatus==1 and i.mode=="Net Banking"):
        return True
    else:
        return False

    

