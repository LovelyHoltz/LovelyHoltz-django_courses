from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Author, Book, Review
import bcrypt

def index(request):
    return render(request,'beltreview_app/index.html')

def register(request):
    valid = User.objects.validateUser(request.POST)
    if valid[0]:
        pw_hash = bcrypt.hashpw(request.POST["password"].encode(),bcrypt.gensalt())
        User.objects.create(email=request.POST["email"], password=pw_hash)
        messages.success(request,"You are registered, Please log in")
    else:
        for error in valid[1]:
            messages.error(request, error)
    return redirect("/")

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST["email"])
        if len(user) > 0:
            user = user[0]
            if bcrypt.checkpw(request.POST["password"].encode(),user.password.encode()):
                request.session["id"] = user.id
                return redirect("/dashboard")
            else:
                messages.error(request, "password does not match")
                return redirect("/")
                messages.error(request, "Cant find email")
            return redirect("/")
    #user = User.objects.filter(email=request.POST["email"])
    #password = request.POST["password"]
    #if bcrypt.checkpw(password.encode(), user.password.encode()):
        #request.session["user_id"] = user.id
        #return redirect("/dashboard")
    #else:
        #messages.error(request, "password does not match")
        #return redirect("/")
        #messages.error(request, "Cant find email")
    #return redirect("/")

def dashboard(request):
    all_reviews = Review.objects.all()
    latest_three_review = all_reviews.order_by("-created_at")[0:3]
    book_ids = []
    for x in latest_three_review:
        book_ids.append(x.book.id)
    context = {
        "latest_three_review": latest_three_review,
        "user": User.objects.get(id=request.session["id"]),
        "other_books": Book.objects.exclude(id__in=book_ids)
    }
    return render(request,'beltreview_app/dashboard.html', context)


def add(request):
    context = {
        "authors":Author.objects.all()
    }
    return render(request,'beltreview_app/add.html',context)

def create(request):
    if request.method == "POST":
        author_name = request.POST["new_author"]
        if author_name == "":
            author_name = request.POST["old_author"]
        author = Author.objects.filter(first_name= author_name)
        if len(author) == 0:
            author = Author.objects.create(first_name = author_name)
        else:
            author = author[0]

        book_title = request.POST["title"]
        book = Book.objects.filter(title=book_title, author=author)
        if len(book) == 0:
            book = Book.objects.create(title = book_title, author=author)
        else:
            book = book[0]

        user = User.objects.get(id = request.session["id"])
        Review.objects.create(revcomment = request.POST["review"], rating = request.POST["rating"], user=user, book=book)
        return redirect("/books/"+str(book.id))
    return redirect("books/add")

def show(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id)
    }
    return render(request, "beltreview_app/showbook.html", context)

def create_reviews(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session["active_id"])
    Review.objects.create(
            book = book,
            user = user,
            revcomment = request.POST["review"],
            rating = request.POST["rating"]
    )
    return redirect("books/{}".format(book_id))

def delete_reviews(request, review_id):
    user = User.objects.get(id=request.session["id"])
    revcomment = Review.objects.get(id=review_id)
    book = review.book.id
    book_id = review.book.id
    if review.user == user:
        revcomment.delete()
    return redirect("/books{}".format(book_id))

def logout(request):
    request.session.clear()
    return redirect("/")
