# from calendar import c
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

from .models import Author, Book
from .forms import BookForm, BookFormSet, AuthorForm, TextForm, NumberForm

def create_book(request, pk):
   author = Author.objects.get(pk=pk)
   books = Book.objects.filter(author=author)
   form = BookForm(request.POST or None)


   if request.method =="POST":
        if form.is_valid():
           book = form.save(commit=False)
           book.author = author
           book.save()
           return redirect("detail-book", pk=book.id)
        else:
           return render(request, "partials/book_form.html", {
               "form": form
           })

   context = {
       "form": form,
       "author": author,
       "books": books
   }

   return render(request, "create_book.html", context)


def create_author(request):
    auth_query = Author.objects.all()
    form = AuthorForm()

    # item = ModelName.objects.gets(attribute='value')
    # item.title = "New Value"
    # item.save()
    if request.method =="POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
           author = form.save(commit=False)
        #    author.name = author.name.lower()
           author.save()
           return redirect("create-author")
        else:
           return render(request, "create_book.html", {
               "form": form
           })
    context = {
        "form": form,
        "authors": auth_query 
    }
    return render(request, "create_author.html", context)

def create_author_form(request):
    form = AuthorForm()
    context = {
        "form": form 
    }
    return render(request, "partials/author_form.html", context)


def create_book_form_number(request):
    form = NumberForm()
    context = {
        "form": form 
    }
    return render(request, "partials/book_form.html", context)


def create_book_form(request):
    form = TextForm()
    context = {
        "form": form 
    }
    return render(request, "partials/book_form.html", context)


def detail_book(request, pk):
    book = Book.objects.get(pk=pk)
    context ={
        "book": book
    }
    return render(request, "partials/book_detail.html", context)


def detail_author(request, pk):
    author = Author.objects.get(pk=pk)
    context ={
        "author": author
    }
    return render(request, "partials/author_detail.html", context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponse('')


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if request.method =="POST":
        if form.is_valid():
           book = form.save()
           return redirect("detail-book", pk=book.id)
        else:
           return render(request, "partials/book_form.html", {
               "form": form,
               "book": book
           })

    context = {
        "form": form,
        "book": book
    }
    return render(request, "partials/book_form.html", context)


# def create_author(request):
#     return render(request, "create_author.html")
