from django.shortcuts import render
from .models import PDFCategory, PDFFile

def pdf_list(request):
    query = request.GET.get('q', '')
    categories = PDFCategory.objects.all()
    
    if query:
        results = PDFFile.objects.filter(title__icontains=query)
    else:
        results = PDFFile.objects.all()
        
    return render(request, 'storage/list.html', {
        'categories': categories,
        'results': results,
        'query': query
    })