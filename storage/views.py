from django.shortcuts import render, redirect, get_object_or_404
from .models import PDFCategory, PDFFile

def pdf_list(request):
    """
    Optional: This view allows searching for PDFs by title.
    You can use this if you want a separate search results page.
    """
    query = request.GET.get('q', '')
    if query:
        results = PDFFile.objects.filter(title__icontains=query)
    else:
        results = PDFFile.objects.all()
        
    return render(request, 'storage/list.html', {
        'results': results,
        'query': query
    })

def upload_pdf(request):
    """
    This view handles the upload of a new PDF. On GET it renders the upload form,
    and on POST it creates a new PDFFile and redirects to the main bookstore view.
    """
    if request.method == "POST":
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        file = request.FILES.get('file')
        
        # You can also add validation here to check for missing fields
        category = get_object_or_404(PDFCategory, id=category_id)
        PDFFile.objects.create(title=title, category=category, file=file)
        return redirect('bookstore')
    else:
        categories = PDFCategory.objects.all()
        return render(request, 'storage/upload.html', {'categories': categories})

def bookstore(request):
    """
    This view will serve as your bookstore front end. It passes all PDF categories,
    and because each PDFCategory has a 'pdfs' related name, you can loop over 
    each category's PDF files in the template.
    """
    categories = PDFCategory.objects.all()
    return render(request, 'bookstore.html', {'categories': categories})
