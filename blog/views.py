from datetime import datetime

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from blog.forms import CommentForm
from blog.models import Post, Comment
from item.models import Item
from projects.models import Project


def frontpage(request):
    items = Item.objects.all()[:3]
    projects = Project.objects.all()[:3]
    posts = Post.objects.all().order_by('-created_on')[:5]
    context = {'items': items, 'posts': posts, 'projects': projects}
    return render(request, 'blog/frontpage.html', context)


def blog_index(request):
    all_posts = Post.objects.all().order_by('-created_on')

    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get('page')
    try:
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        posts = paginator.get_page(page_number)
    except EmptyPage:
        posts = paginator.get_page(page_number)
    context = {'posts': posts}
    return render(request, 'blog/blog_index.html', context)


def blog_category(request, category):
    all_posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get('page')
    try:
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        posts = paginator.get_page(page_number)
    except EmptyPage:
        posts = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'blog/blog_category.html', context)


def blog_detail(request, id):
    post = Post.objects.get(id=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                owner=request.user,
                body=form.cleaned_data['body'],
                post=post,
                edited='',
                last_modified=datetime.now(),

            )
            comment.save()
            messages.info(request, "Comment submitted successfully!")
            return redirect('blog:blog-detail', post.id)

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog/blog_detail.html', context)


def edit_comment(request, id):
    comment = Comment.objects.get(id=id)
    post = comment.post
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            comment.last_modified = datetime.now()
            comment.edited = 'Edited',
            form.save()
            return redirect('blog:blog-detail', post.id)
    context = {'comment': comment, 'post': post, 'form': form}
    return render(request, 'blog/edit_comment.html', context)
