from django import forms
from django.forms.models import(
    inlineformset_factory, 
    formset_factory, 
    modelform_factory, 
    modelformset_factory
)
from .models import Book, Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',)

class TextForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            "title",
            "text"
        )

class NumberForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            "title",
            "number"
        )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            "title",
            "text"
        )


BookFormSet = inlineformset_factory(
    Author,
    Book,
    BookForm,
    AuthorForm,
    can_delete=False,
    min_num=2,
    extra=0
)
            