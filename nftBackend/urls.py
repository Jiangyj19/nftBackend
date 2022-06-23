from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('query/', include('queryContract.urls')),
    path('sign/', include('signMsg.urls')),
    path('admin/', admin.site.urls),
]