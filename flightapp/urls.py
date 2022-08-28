from django.urls import path

from . import views



urlpatterns = [
    path('', views.homeView, name='home'),
    path('about/', views.aboutView, name='about'),
    
    path('shop/', views.shopView, name='shop'),
    path('shop-detail/<str:id>/', views.shopdetailView, name='shopdetail'),
    
    path('cart/', views.cartView, name='cart'),
    path('add-cart/<str:id>/', views.addCartView, name='add-cart'),
    path('remove-cart/<str:id>/', views.removeCartView, name='remove-cart'),
    
    path('wishlist/', views.wishlistView, name='wishlist'),
    path('add-wishlist/<str:id>/', views.addWishlistView, name='add-wishlist'),
    path('remove-wishlist/<str:id>/', views.removeWishlistView, name='remove-wishlist'),
    
    path('contact/', views.contactView, name='contact'), 
]
