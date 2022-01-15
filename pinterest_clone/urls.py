from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pinterest.urls', namespace='pinterest')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('boards/', include('boards.urls', namespace='boards')),
    path('pins/', include('pins.urls', namespace='pins')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)