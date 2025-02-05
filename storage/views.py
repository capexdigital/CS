from django.shortcuts import render, redirect
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

def upload_pdf(request):
    if request.method == "POST":
        title = request.POST['title']
        category_id = request.POST['category']
        file = request.FILES['file']
        cover = request.FILES.get('cover')
        category = PDFCategory.objects.get(id=category_id)
        PDFFile.objects.create(title=title, category=category, file=file, cover=cover)
        return redirect('pdf_list')
    else:
        categories = PDFCategory.objects.all()
        return render(request, 'storage/upload.html', {'categories': categories})

def bookstore(request):
    query = request.GET.get('q', '')
    categories = PDFCategory.objects.all()
    
    if query:
        pdf_files = PDFFile.objects.filter(title__icontains=query)
    else:
        pdf_files = PDFFile.objects.all()
        
    return render(request, 'bookstore.html', {'categories': categories, 'pdf_files': pdf_files, 'query': query})