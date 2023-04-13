from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.

def mainpage(request):
    blogs = Blog.objects.all()  # 해당 객체의 모든 내용을 담겠다 -> Blog에 있는 모든 내용들을 담는다는 뜻
    return render(request, 'main/mainpage.html', {'blogs':blogs})

def secondpage(request):
    return render(request, 'main/secondpage.html')

def new(request):
    return render(request, 'main/new.html')

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'main/detail.html', {'blog':blog})

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']

    new_blog.save()

    return redirect('detail', new_blog.id)