from django.urls import path

from . import views



urlpatterns = [
    path('', views.profileView, name='profile'),
    path('login/', views.loginView, name='login'),
    path('cart/', views.cartView, name='cart'),

    path('faq/', views.faqView, name='faq'),
    path('error/', views.errorView, name='error'),
    
    path('empty/', views.emptyView, name='empty'),
    path('thanks/', views.thanksView, name='thanks'),
    
    path('chekout/', views.chekoutView, name='chekout'),

    path('wishlist/', views.wishlistView, name='wishlist'),
    path('coming-soon/', views.comingView, name='coming-soon'),
    
]