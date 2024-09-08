from django.shortcuts import get_object_or_404, render

from details.models import Book

def book_detail(request,pk):
    book=get_object_or_404(Book,pk=pk)
    context={
        'book':book,
    }
    return render(request,'book_detail.html',context)