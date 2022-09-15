from django.urls import path

from . import views


urlpatterns = [
    path('', views.homeView, name='home'),
    path('search/', views.searchView, name='search'),
    path('about/', views.aboutView, name='about'),
    path('yandex_4bc38c819937bed7.html/', views.yandexView, name='yandex'),

    path('shop/', views.shopView, name='shop'),
    path('shop-detail/<str:id>/', views.shopdetailView, name='shopdetail'),
    path('shop-detail/<int:id>/', views.commentRemove, name='remove'),

    path('cart/', views.cartView, name='cart'),
    path('add-cart/<str:id>/', views.addCartView, name='add-cart'),
    path('remove-cart/<int:id>/', views.removeCartView, name='remove-cart'),

    path('wishlist/', views.wishlistView, name='wishlist'),
    path('add-wishlist/<str:id>/', views.addWishlistView, name='add-wishlist'),
    path('remove-wishlist/<int:id>/',
         views.removeWishlistView, name='remove-wishlist'),


    path('contact/', views.contactView, name='contact'),
]
