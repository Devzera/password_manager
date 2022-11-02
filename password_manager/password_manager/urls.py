from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('users.urls', namespace='accounts')),
    path('about/', include('about.urls', namespace='about')),
    path('api/', include('api.urls', namespace='api')),
    path('', include('generator.urls', namespace='passwords')),
]
