from django.urls import path

from . import views



urlpatterns = [
    path('', views.homeView, name='home'),
    path('about/', views.aboutView, name='about'),
    path('shop/', views.shopView, name='shop'),
    path('shop-detail/', views.shopdetailView, name='shopdetail'),
    path('contact/', views.contactView, name='contact'), 
]
