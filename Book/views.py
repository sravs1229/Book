from django.shortcuts import render

from details.models import Book

def home(request):
        book=Book.objects.all()
        context={
                'book':book,
        }
        return render(request,'home.html',context)