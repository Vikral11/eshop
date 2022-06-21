
from django.contrib import admin
from django.urls import path
from mainApp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', views.login),
    path('signup/', views.signup),
    path('logout/', views.logout),
    path('profile/', views.profile),
    path("updateseller/", views.updateseller),
    path("addproducts/", views.addproducts),
    path("deleteproduct/<int:id>", views.delpro),
    path("updateproduct/<int:id>", views.updpro),
    path("shop/<str:mains>/<str:sub>/<str:bran>/<str:fil>/", views.shop),
    path("product_page/<int:id>/", views.productp),
    path("updatebuyer/", views.updatebuyer),
    path("wishlist/<int:id>/", views.wishlistt),
    path("removeproduct/<int:id>",views.removeproduct),
    path("AddToCart/<int:id>/", views.AddToCart),
    path("cart/", views.cart),
    path("rcart/<int:id>/", views.rcart),
    path("ucart/<int:id>/<int:num>/", views.ucart),
    path("checkout/",views.checkouts),
    path("orderplaced/",views.orderplaced),
    path("orderplaced/",views.orderplaced),
    path("paymentSuccess/<str:rppid>/<str:rpoid>/<str:rpsid>/<str:chid>",views.paymentsuccess),
    path("paynow/<int:id>/", views.paynow),
    path("newsletter/", views.Newsletter),
    path("contactus/", views.contact),
    path("forgetpassword-email/", views.forgetpass_email),
    path("forgetpass_otp/", views.forgetpass_otp),
    path("forgetpass_newpass/", views.forgetpass_newpass),
    path("orderhistory/",views.sellerorders),
    path("updateorderhis/<int:id>/", views.updateorderhistory),
    path("about/", views.about),
    

    
    

] + static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
