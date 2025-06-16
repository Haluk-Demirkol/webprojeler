from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iptal/', include('iptal.urls', namespace='iptal')),
    path('tesekkur_simple/', include('iptal.urls')),
    path('tesekkur_wait/', include('iptal.urls')),
    path('', include('iptal.urls', namespace='iptal'))
]
