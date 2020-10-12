from django.shortcuts import render, redirect,get_object_or_404
from .models import BookShelf
from home.models import Post, Book
from .forms import BookShelfUpdate
# Create your views here.
"""back_newBookShelf.html로 이동하는 함수"""
def newBookShelf(request):
    return render(request, 'back_newBookShelf.html')
"""detail.html로 이동하는 함수"""
def detail(request):
    return render(request, 'detail.html')

"""책장 생성 함수 """
def createBookShelf(request):
    bookShelf = BookShelf()
    bookShelf.username = request.user
    bookShelf.postID = request.POST.get('postID')
    bookShelf.bookShelfTitle = request.GET['bookShelfTitle']
    bookShelf.save()
    request.user.profile.bookShelf.add(bookShelf.id)

    return redirect('/back_myPage/')

"""back_myPage.html 로 이동하는 함수. """
def myPage(request):
    bookShelves = BookShelf.objects.all()

    return render(request, 'myPage.html', {'bookShelves': bookShelves, 'posts': request.user.profile.postID.all})

"""책장 삭제 함수"""
def deleteBookShelf(request, bookShelf_id):
    BookShelf.objects.get(id=bookShelf_id).delete()
    return redirect('/back_myPage')

"""책장 수정 함수"""
def updateBookShelf(request, bookShelf_id):
    bookShelf = get_object_or_404(BookShelf,pk=bookShelf_id)
    bookShelves = BookShelf.objects.all()
    posts = Post.objects.all()

    if request.method =='POST':
        form = BookShelfUpdate(request.POST)
        if form.is_valid():
            bookShelf.bookShelfTitle = form.cleaned_data['bookShelfTitle']
            bookShelf.save()
            return render(request,'back_myPage.html',{'bookShelves': bookShelves, 'posts': posts})
    else:
        form = BookShelfUpdate(instance = bookShelf)
    return render(request,'back_updateBookShelf.html', {'form':form})
