from django.shortcuts import render, get_object_or_404

from books.models import Book


# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, "index.html", context)

def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, "book_list.html", context)

def book_detail(request, pk):
    book = get_object_or_404(Book,pk=pk)

    context = {
        'book': book
    }
    return render(request, "book/book_detail.html", context)