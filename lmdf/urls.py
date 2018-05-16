from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('lmdf/', include('lmdf.urls')),
    path('admin/', admin.site.urls),
]