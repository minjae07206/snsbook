from django.shortcuts import render, redirect
from .models import CustomUser, Post
from django.contrib.auth.decorators import login_required



# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        print(email)
    return render(request, 'login.html')

@login_required(login_url='login')
def index(request):
    all_posts = Post.objects.all()
    
    return render(request, "index.html", {"all_posts": all_posts})

def create(request):
    if request.method == "POST":
        user = request.user.username
        image = request.FILES.get("photo")
        caption = request.POST['caption']
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    return render(request, 'create.html')

def search(request):
    if request.method == "POST":
        searched_posts = Post.objects.filter(caption__icontains=request.POST["search"])
        searched_posts = list(searched_posts)
        print(searched_posts)
        return render(request, 'search.html', {'searched_posts': searched_posts})
    return render(request, 'index.html')

def settings(request):
    return render(request, 'settings.html')