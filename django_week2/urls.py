
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo_gallery_app.urls')), 
    path('accounts/',include('registration.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/',include('api.urls'))
]
                                