from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('query/', include('queryContract.urls')),
    path('admin/', admin.site.urls),
]