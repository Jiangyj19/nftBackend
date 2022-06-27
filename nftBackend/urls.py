from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('query/', include('query.urls')),
    path('sign/', include('sign.urls')),
    path('admin/', admin.site.urls),
]