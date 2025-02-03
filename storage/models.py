from django.db import models

class PDFCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PDFFile(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(PDFCategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title