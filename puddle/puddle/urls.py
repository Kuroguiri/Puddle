from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import index, contact, about

urlpatterns = [
    path('', index, name='index.html'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
