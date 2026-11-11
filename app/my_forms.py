from django import forms

from app.models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('names', 'phone','email')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'year', 'cost')