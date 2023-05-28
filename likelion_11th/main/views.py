from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment, Tag
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
    if request.method == 'GET':
        comments = Comment.objects.filter(blog=blog)
        return render(request, 'main/detail.html',  {
            'blog' :blog,
            'comments' : comments,
        })
    elif request.method == "POST":
        new_comment = Comment()
        new_comment.blog = blog
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.pub_data = timezone.now()
        new_comment.save()
        return redirect('main:detail', id)

def create(request):
    if request.user.is_authenticated:
        new_blog = Blog()
        new_blog.title = request.POST['title']
        new_blog.writer = request.user
        new_blog.pub_date = timezone.now()
        new_blog.body = request.POST['body']
        new_blog.image = request.FILES.get('image')

        new_blog.save()

        words = new_blog.body.split(' ')
        tag_list = []
        for w in words:
            if len(w) > 0:
                if w[0] == '#':
                    tag_list.append(w[1:])
        
        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_blog.tags.add(tag.id)
        return redirect('main:detail', new_blog.id)
    else :
        return redirect('accounts:login')

def edit(request, id):
    edit_blog = Blog.objects.get(id = id)
    return render(request, 'main/edit.html', {'blog' : edit_blog})

def update(request, id):
    if request.user.is_authenticated:
        new_blog = Blog.objects.get(id = id)
        new_blog.title = request.POST['title']
        new_blog.writer = request.POST['writer']
        new_blog.pub_date = timezone.now()
        new_blog.body = request.POST['body']

        new_blog.save()

        return redirect('main:detail', new_blog.id)
    return redirect('accounts:login')

def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('main:mainpage')

def tag_list(request):
    tags =  Tag.objects.all()
    return render(request, 'main/tag_list.html', {
        'tags' : tags,
    })

def tag_blogs(request, tag_id):
    tag = get_object_or_404(Tag, id = tag_id)
    blogs = tag.blogs.all()
    return render(request, 'main/tag_blogs.html', {
        'tag' :tag,
        'blogs' : blogs,
    })