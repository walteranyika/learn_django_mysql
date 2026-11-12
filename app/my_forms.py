from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from app.models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('names', 'phone','email')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'year', 'cost', 'cover')

class CustomSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=5030)
    last_name = forms.CharField(required=True, max_length=5030)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Automatically add Bootstrap's 'form-control' class to every field
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control radius-0"

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'username', 'email','password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomLoginForm(AuthenticationForm):
    # # Optional: Add a "Remember Me" checkbox
    # remember_me = forms.BooleanField(
    #     required=False,
    #     widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add Bootstrap classes and placeholders to username & password
        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Enter your username",
            "autofocus": True,
        })
        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Enter your password",
        })