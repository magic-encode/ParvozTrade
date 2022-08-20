from django.urls import path

from . import views



urlpatterns = [
    path('', views.homeView, name='home'),
    path('about/', views.aboutView, name='about'),
    path('shop/', views.shopView, name='shop'),
    path('blog/', views.blogView, name='blog'),
    path('contact/', views.contactView, name='contact'),
]
