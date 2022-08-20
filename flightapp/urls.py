from django.urls import path

from . import views



urlpatterns = [
    path('', views.homeView, name='home'),
    path('about/', views.aboutView, name='about'),
    path('shop/', views.shopView, name='shop'),
    path('shop-detail/', views.shopdetailView, name='shopdetail'),
    path('blog-detail/', views.blogdetailView, name='blogdetail'),
    path('blog/', views.blogView, name='blog'),
    path('contact/', views.contactView, name='contact'),
    
    # -----------------------------------------
    path('profile/', views.profileView, name='profile'),
    path('login/', views.loginView, name='login'),
    path('cart/', views.cartView, name='cart'),
    
]
