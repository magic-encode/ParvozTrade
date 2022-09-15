from django.contrib import admin
from django.conf import settings

from django.urls import path
from django.urls import re_path
from django.urls import include

from django.views.static import serve

from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from flightapp.views import robots_txt

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("robots.txt", robots_txt),
    path('', include('flightapp.urls')),
    path('user/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset_email.html"),
         name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
         name="password_reset_complete"),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]