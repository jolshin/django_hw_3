from django.shortcuts import render, redirect

from books.models import Book

def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    books =  Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)

def books_by_date(request, slug):
    template = 'books/books_by_date.html'
    books =  Book.objects.all()

    #didn't find a solution of a problem (page pagination by pub_date) with Paginator 
    #so I made my own:

    # sort tuple of all possible pages (for pagination)
    pages = sorted(tuple(set(book.slug for book in books)))

    # assign values for next and previous pages
    if pages.index(slug) + 1 == len(pages):
        next_page = pages[0]
    else:
        next_page = pages[pages.index(slug) + 1]
    previous_page = pages[pages.index(slug) - 1]

    context = {
        'books': books,
        'cur_page': slug,
        'next_page': next_page,
        'previous_page': previous_page
    }
    return render(request, template, context)
