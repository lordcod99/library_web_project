from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import book
from comments.models import comment
from orders.models import order
from profiles.models import user_profile
from .forms import review_form
# Create your views here.
def home_veiw(request, *args, **kwrgs):
    return render(request, 'home.html')

def books_veiw(request, *args, **kwrgs):
    books= book.objects.all().order_by('-n_read')
    context={'books': books}
    return render(request, 'books/books.html', context)


def book_veiw(request, book_id,*args, **kwrgs):
    books=get_object_or_404(book, pk=book_id)
    comments =comment.objects.filter(book = book_id)
    form = review_form(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        user = user_profile.objects.filter(name = request.user.username).first()
        obj.user = user
        obj.book=books
        obj.save()
        form = review_form()
    count = len(comments)
    context={'books': books, "comments":comments, "count":count, "form":form}
    return render(request, 'books/book.html', context)



