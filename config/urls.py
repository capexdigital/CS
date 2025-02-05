from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from storage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bookstore, name='bookstore'),
    path('pdfs/', views.pdf_list, name='pdf_list'),
    path('upload/', views.upload_pdf, name='upload_pdf'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
