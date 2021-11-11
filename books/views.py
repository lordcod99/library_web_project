from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import book
# Create your views here.
def home_veiw(request, *args, **kwrgs):
    return render(request, 'home.html')

def books_veiw(request, *args, **kwrgs):
    books= book.objects.all().order_by('-n_read')
    context={'books': books}
    return render(request, 'books/books.html', context)


def book_veiw(request, book_id,*args, **kwrgs):
    books=get_object_or_404(book, pk=book_id)
    context={'books': books}
    return render(request, 'books/book.html', context)

