from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from app.models import Author, Book
from app.my_forms import AuthorForm, BookForm


def authors(request):
    authors = Author.objects.all() # select * from authors
    # authors = Author.objects.count() # Select count(*) from authors
    # authors = Author.objects.filter(title__icontains='django')
    # authors = Author.objects.filter(Q(names__icontains='django') | Q(email__icontains='django'))
    # authors = Author.objects.filter(Q(names__icontains='django') & ~Q(email__icontains='django'))
    return render(request, 'authors.html', {'authors': authors})


def books(request):
    books = Book.objects.all()
    # books = Book.objects.count()
    # books = Book.objects.filter(cost__gt=400)
    books = Book.objects.filter(author__id=1)
    return render(request, 'books.html',{'books': books})


def details(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, 'details.html', {'book': book})


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('authors')
    else:
        form = AuthorForm()

    return render(request, 'create_author.html', {'form': form})


def create_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('books')
    else:
        form = BookForm()

    return render(request, 'create_books.html', {'form': form})