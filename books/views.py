from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import book
from comments.models import comment
from orders.models import order
from profiles.models import user_profile
from .forms import review_form, search_form
from collections import deque
# Create your views here.
def home_veiw(request, *args, **kwrgs):
    return render(request, 'home.html')

def books_veiw(request, *args, **kwrgs):
    ls= book.objects.all().order_by('-n_read')
    genre_list = deque([])
    for s in list(set((ls.values_list("genre", flat=True)))):
        if ',' in s:
            for e in s.split(','):
                if e not in genre_list:
                    genre_list.append(e)
        elif s not in genre_list:
            genre_list.append(s)

    authors_list = deque([])
    for s in list(set((ls.values_list("authors", flat=True)))):
        if ',' in s:
            for e in s.split(','):
                if e not in authors_list:
                    authors_list.append(e)
        elif s not in authors_list:
            authors_list.append(s)



    if request.POST.get("select_genre") != None:
        new_ls = deque([])
        for b in ls:
            if request.POST.get("select_genre") in b.genre:
                new_ls.append(b)
        ls = new_ls

    if request.POST.get("select_author") != None:
        new_ls = deque([])
        for b in ls:
            if request.POST.get("select_author") in b.authors:
                new_ls.append(b) 
        ls = new_ls


    my_form = search_form(request.POST or None)
    if my_form.is_valid():
        data = my_form.cleaned_data.get("search")
        # print("###################")
        # print(data)

        new_ls = deque([])
        for b in ls:
            if (data.lower() in b.name.lower()) or (data.lower() in b.genre.lower()) or (data.lower() in b.authors.lower()):
                new_ls.append(b)

        ls = new_ls
    
    if len(ls)==0:
        no_b = True
    else:
        no_b = False
    context={"ls":ls, "no_b":no_b, "genre_list":genre_list, "author_list":authors_list}
    return render(request, 'books/books.html', context)


def book_veiw(request, book_id,*args, **kwrgs):
    books=get_object_or_404(book, pk=book_id)
    user = user_profile.objects.filter(name = request.user.username).first()
    comments =comment.objects.filter(book = book_id)
    form = review_form(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # user = user_profile.objects.filter(name = request.user.username).first()
        obj.user = user
        obj.book=books
        obj.save()
        form = review_form()

    stat = ''
    if request.method == "POST":
        odr = order.objects.create(book = books, user = user)
        stat = odr.r_status

    qs = order.objects.all().filter(book = books).filter(user = user).exclude(r_status = "returned")
    if len(qs):
        qs = qs.first()
        stat = qs.r_status
    

    count = len(comments)
    context={'books': books, "comments":comments, "count":count, "form":form, "stat":stat}
    return render(request, 'books/book.html', context)

def book_main_view(request, *args, **kwrgs):
    books= book.objects.all().order_by('-n_read')[:10]
    context={'ls': books}
    return render(request, 'books/book_main.html', context)

