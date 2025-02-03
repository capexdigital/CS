from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pdf_storage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pdf_list, name='pdf_list'),
]

# This enables file uploads during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)