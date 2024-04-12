import requests
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from blog.models import Post, Contact, Comment


def index_view(request):
    posts = Post.objects.filter(is_published=True)
    d = {
        'posts': posts,
        'home': 'active'
    }
    return render(request, 'index.html', context=d)


def blog_view(request):
    data = request.GET
    cat = data.get('cat')
    page = data.get('page', 1)
    if cat:
        posts = Post.objects.filter(is_published=True, category_id=cat)
    else:
        posts = Post.objects.filter(is_published=True)
    post_obj = Paginator(posts, 3)
    d = {
        'posts': post_obj.page(page),
        'blog': 'active'
    }
    return render(request, 'blog.html', context=d)


def blog_single_view(request, pk):
    post = Post.objects.filter(id=pk).first()
    if request.method == 'POST':
        data = request.POST
        obj = Comment.objects.create(post_id=pk, name=data.get('name'), message=data.get('message'),
                                     email=data.get('email'))
        obj.save()
        return redirect(f'/blog/{pk}')
    comments = Comment.objects.filter(post_id=pk)
    d = {
        'post': post,
        'comments': comments
    }
    return render(request, 'blog-single.html', context=d)


def about_view(request):
    d = {
        'about': 'active'
    }
    return render(request, 'about.html', context=d)


def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        obj = Contact.objects.create(name=data.get('name'), email=data.get('email'), message=data.get('message'),
                                     subject=data.get('subject'))
        obj.save()
        token = "6912718237:AAH2v2r4x2TuYnHqfpbi1ci43AxYKEiBWoE"
        requests.get(
            f"""https://api.telegram.org/bot{token}/sendMessage?chat_id=5093765356&text=MOOSE\nid: {obj.id}\nname: {obj.name}\nemail: {obj.email}""")

        return redirect('/contact')
    return render(request, 'contact.html')
