from django.contrib import admin
from .models import PDFCategory, PDFFile

class PDFFileInline(admin.TabularInline):
    model = PDFFile
    extra = 1

@admin.register(PDFCategory)
class PDFCategoryAdmin(admin.ModelAdmin):
    inlines = [PDFFileInline]

admin.site.register(PDFFile)