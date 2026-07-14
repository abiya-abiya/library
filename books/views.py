from django.shortcuts import render

from books.models import Book


# Create your views here.
def index(request):
    return render(request, "index.html")

def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, "book_list.html", context)