from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('generator/', include('generator.urls', namespace='generator')),
    path('admin/', admin.site.urls),
]
