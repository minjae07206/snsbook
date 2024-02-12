from django.shortcuts import render, redirect
from .models import CustomUser, Post


# Create your views here.

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
    return render(request, 'index.html')

def settings(request):
    return render(request, 'settings.html')