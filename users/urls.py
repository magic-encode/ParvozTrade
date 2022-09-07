from django.urls import path

from . import views

from .views import blogDetailView



urlpatterns = [
    path('', views.profileView, name='profile'),
    path('register/', views.registerUser, name='register'),
    
    path('blog/', views.blogView, name='blog'),
    path('blog/<str:id>/', views.blogDetailView, name='blogdetail'),
    
    
    path('editAccount/', views.editAccount, name='edit'),
    path('uzgardi/', views.uzgarView, name='uzgardi'),
    

    path('faq/', views.faqView, name='faq'),
    path('error/', views.errorView, name='error'),
    
    path('empty/', views.emptyView, name='empty'),
    path('thanks/', views.thanksView, name='thanks'),
    
    path('checkout/<str:id>/', views.chekoutView, name='chekout'),
    path('finish_shop/', views.finishView, name='finish_shop'),
    
    

    path('coming-soon/', views.comingView, name='coming-soon'),
    
]