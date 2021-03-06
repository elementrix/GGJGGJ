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

"""책장 생성 함수 수정요함"""
def createBookShelf(request):
    title = request.GET['bookShelfTitle']
    bookShelves = BookShelf.objects.all()
    if (title==""):
       return render(request, 'myPage.html', {'bookShelves': bookShelves, 'posts': request.user.profile.postID.all}) 
    bookShelf = BookShelf()
    bookShelf.username = request.user
    # bookShelf.postID.add(request.POST.get('postID'))
    bookShelf.bookShelfTitle = title
    bookShelf.save()
    request.user.profile.bookShelf.add(bookShelf.id)
    return render(request, 'myPage.html', {'bookShelves': bookShelves, 'posts': request.user.profile.postID.all})

"""back_myPage.html 로 이동하는 함수. """
def myPage(request):
    bookShelves = BookShelf.objects.all()

    return render(request, 'myPage.html', {'bookShelves': bookShelves, 'posts': request.user.profile.postID.all})

"""책장 삭제 함수""" 
def deleteBookShelf(request, bookShelf_id):
    # print(BookShelf.objects.get(id=bookShelf_id).postID.all)
    # for po in BookShelf.objects.get(id=bookShelf_id).postID.all():
    #     print(po.id)
    bookShelf = BookShelf.objects.get(id=bookShelf_id)
    for post in bookShelf.postID.all():
        print(post.id)
        post.delete()
    bookShelf.delete()
    return redirect('/back_myPage')

"""책장 수정 함수"""
def updateBookShelf(request, bookShelf_id,):
    bookShelf = get_object_or_404(BookShelf,pk=bookShelf_id)
    bookShelves = BookShelf.objects.all()
    posts = Post.objects.all()

    if request.method =='POST':
        form = BookShelfUpdate(request.POST)
        if form.is_valid():
            bookShelf.bookShelfTitle = form.cleaned_data['bookShelfTitle']
            bookShelf.save()
            return render(request,'myPage.html',{'bookShelves': bookShelves, 'posts': posts})
    else:
        form = BookShelfUpdate(instance = bookShelf)
    return render(request,'back_updateBookShelf.html', {'form':form})
