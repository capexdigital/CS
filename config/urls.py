from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from storage import views  # Changed import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pdf_list, name='pdf_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)