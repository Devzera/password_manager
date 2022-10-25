from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('users.urls', namespace='accounts')),
    path('', include('generator.urls', namespace='passwords')),
    # path('', include('storage.urls', namespace='passwords')),
]
