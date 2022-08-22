from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('flightapp.urls')),
    path('user/', include('users.urls')),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
