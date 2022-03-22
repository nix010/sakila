from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from api import settings
from sakila.urls import router as sakila_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sakila/', include(sakila_router.urls)),
    path('sakila/', include('sakila.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

