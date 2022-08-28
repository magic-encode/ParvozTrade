from django.urls import path

from . import views



urlpatterns = [
    path('', views.homeView, name='home'),
    path('about/', views.aboutView, name='about'),
    path('shop/', views.shopView, name='shop'),
    path('shop-detail/<str:id>/', views.shopdetailView, name='shopdetail'),
    path('add-cart/<str:id>/', views.addCartView, name='add-cart'),
    path('contact/', views.contactView, name='contact'), 
]
