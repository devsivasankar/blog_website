from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils import timezone





def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request,'Username Already Exist')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'Email is Already in Use')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request,'Account Created Succussfully, You can Login Now...')
                return redirect('login')
        else:
            messages.error(request,'Password Does Not Match')    
    return render(request, 'signup.html')





def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Succussfully')
            return redirect('index')
        else:
            messages.error(request,'Invalid Username or Password')
    return render(request, 'login.html')


def Logout(request):
    logout(request)
    messages.success(request,'You have been logged out successfully.')
    return redirect('index')






def Index(request):
    query = request.GET.get('q')  # Get the search query from the URL
    if query:
        # Filter blogs based on title or content containing the query
        adminblog = Adminblog.objects.filter(
            title__icontains=query
        ) | Adminblog.objects.filter(content__icontains=query)
    else:
        # No search query, fetch all blogs ordered by published date
        adminblog = Adminblog.objects.all().order_by('-published_date')
    
    return render(request, 'index.html', {'adminblogvar': adminblog, 'query': query})



def Blog_detail(request, pk):
    post = get_object_or_404(Adminblog, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content')
        if content.strip():  # Ensure the comment is not empty
            Comments.objects.create(
                post=post,
                user=request.user,
                content=content,
            )
            return redirect('blog_details', pk=post.pk)  # Redirect to the same page after submitting a comment

    return render(request, 'blog_detail.html', {
        'post': post,
        'comments': comments,
    })


@login_required
def save_bookmark(request, pk):
    blog = get_object_or_404(Adminblog, pk = pk)
    Bookmark.objects.get_or_create(user = request.user, blog = blog)
    return redirect('collection')


@login_required
def collection(request):
    bookmarks = Bookmark.objects.filter(user = request.user)
    return render(request, 'collection.html', {'bookmark':bookmarks})


@login_required
def remove_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, user=request.user, blog_id=pk)
    bookmark.delete()
    messages.success(request, 'Bookmark removed successfully.')
    return redirect('collection')


@login_required
def Userblog(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES.get('image')
        content = request.POST['content']
        # save user blogs
        Adminblog.objects.create(
            user = request.user,
            title = title,
            image = image,
            content = content,
            published_date = timezone.now(),
        )
        messages.success(request, 'Your Blog is Posted Succussfully and Your Blog is Live Now')
        return redirect('index')
    return render(request, 'Userblog.html')


def error404(request,exception):
    return render(request,'error404.html')
