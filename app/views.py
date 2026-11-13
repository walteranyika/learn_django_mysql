from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from app.models import Author, Book
from app.my_forms import AuthorForm, BookForm, CustomSignUpForm, CustomLoginForm


@login_required
def authors(request):
    authors = Author.objects.all() # select * from authors
    # authors = Author.objects.count() # Select count(*) from authors
    # authors = Author.objects.filter(title__icontains='django')
    # authors = Author.objects.filter(Q(names__icontains='django') | Q(email__icontains='django'))
    # authors = Author.objects.filter(Q(names__icontains='django') & ~Q(email__icontains='django'))
    return render(request, 'authors.html', {'authors': authors})

@login_required
def books(request):
    books = Book.objects.all()
    # books = Book.objects.count()
    # books = Book.objects.filter(cost__gt=400)
    books = Book.objects.filter(author__id=1)
    return render(request, 'books.html',{'books': books})

@login_required
def details(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, 'details.html', {'book': book})

@login_required
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            messages.success(request, 'Author created successfully')
            return redirect('authors')
    else:
        form = AuthorForm()

    return render(request, 'create_author.html', {'form': form})

@login_required
def create_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Book created successfully')
            return redirect('books')
    else:
        form = BookForm()

    return render(request, 'create_books.html', {'form': form})

@login_required
@permission_required('app.change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully')
            return redirect('books')
    else:
        form = BookForm(instance=book)
    return render(request, 'create_books.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # next_url = request.GET.get('next','authors')
            # return redirect(next_url)
            messages.success(request, 'Login successful')
            return redirect('authors')
    else:
        form = CustomLoginForm()
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = CustomSignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def signout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('authors')

def custom_404(request, exception):
    return render(request, "errors/404.html", {"path": request.path},status=404)