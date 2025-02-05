# filepath: storage/admin.py
from django.contrib import admin
from .models import PDFCategory, PDFFile

@admin.register(PDFCategory)
class PDFCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(PDFFile)
class PDFFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at')