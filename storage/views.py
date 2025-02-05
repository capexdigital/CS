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
        # Process the uploaded PDF file:
        # For example, you might use a form to handle file uploads.
        # After processing, redirect to the PDF list or show a success message.
        return redirect('pdf_list')
    else:
        # Render a template with an upload form
        return render(request, 'storage/upload.html')
