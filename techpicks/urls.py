from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('authentication.urls')),
    path('auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]