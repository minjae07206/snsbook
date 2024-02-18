from django.shortcuts import render, redirect
from .models import CustomUser, Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Username or password invalid.")
    return render(request, 'signin.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Account with the email already exists")
            return redirect('signup')
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
            return redirect('signup')
        else:
            new_user = CustomUser.objects.create_user(username=username, password=password, email=email)
            new_user.save()
            return redirect('login')
    return render(request, 'signup.html')

def signout(request):
    if request.method == "POST":
        logout(request)
        return redirect('signin')

@login_required(login_url="signin")
def index(request):
    all_posts = Post.objects.all()
    
    return render(request, "index.html", {"all_posts": all_posts})

def profile(request):
    return render(request, 'profile.html')

@login_required(login_url="signin")
def create(request):
    if request.method == "POST":
        user = request.user.username
        image = request.FILES.get("photo")
        caption = request.POST['caption']
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    return render(request, 'create.html')

@login_required(login_url="signin")
def search(request):
    if request.method == "POST":
        searched_posts = Post.objects.filter(caption__icontains=request.POST["search"])
        searched_posts = list(searched_posts)
        print(searched_posts)
        return render(request, 'search.html', {'searched_posts': searched_posts})
    return render(request, 'index.html')

@login_required(login_url="signin")
def settings(request):
    return render(request, 'settings.html')