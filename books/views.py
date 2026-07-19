from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect

from books.forms import BookForm
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
    query = request.GET.get("q")
    title = request.GET.get("title")
    author = request.GET.get("author")
    year = request.GET.get("year")

    if query:
        books = books.filter(title__icontains=query)
    if title:
        books = books.filter(title__icontains=title)
    if author:
        books = books.filter(author__icontains=author)
    if year:
        books = books.filter(year__icontains=year)


    context = {
        'books': books,
        'query': query,
        'title': title,
        'author': author,
        'year': year,
    }
    return render(request, "book_list.html", context)

def book_detail(request, pk):
    book = get_object_or_404(Book,pk=pk)

    context = {
        'book': book
    }
    return render(request, "book/book_detail.html", context)


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    context = {
        'form': form
    }
    return render(request, "book/book_create.html", context)

def book_update(request, pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm(instance=book)
    context = {
        'form': form
    }
    return render(request, "book/book_update.html", context)


def book_delete(request, pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('index')
    context = {
        'book': book
    }
    return render(request, "book/book_delete.html", context)



def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('index')