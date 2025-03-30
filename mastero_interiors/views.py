from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .forms import MeetDesignerForm
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from .models import BlogPost
from .forms import BlogPostForm


def mastero_interiors(request):
    if request.method == 'POST':
        form = MeetDesignerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message'] + ' '+ email

            # Send email
            send_mail(
                f'Meet a Designer Request from {name}',
                message,
                email,
                ['srihome023@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Thank you! Your request has been submitted.')
            return redirect('index')
    else:
        form = MeetDesignerForm()

    return render(request, 'mastero_interiors/index.html', {'form': form})

def blog_page(request, pk=None):
    if pk is not None:
        # Fetch the blog post by primary key if pk is provided
        post = get_object_or_404(BlogPost, pk=pk,active=True)
    else:
        # Fetch the latest blog post if no pk is provided
        post = BlogPost.objects.filter(active=True).latest('created_at')

    # Increment the view count
    post.views += 1
    post.save()

    # Get previous and next posts
    previous_post = BlogPost.objects.filter(created_at__lt=post.created_at,active=True).order_by('-created_at').first()
    next_post = BlogPost.objects.filter(created_at__gt=post.created_at,active=True).order_by('created_at').first()

    # Fetch popular blogs based on views
    popular_posts = BlogPost.objects.filter(active=True).order_by('-views')[:5]


    print("post ", post)
    context = {
        'post': post,
        'popular_posts': popular_posts,
        'previous_post': previous_post,
        'next_post': next_post,
    }
    
    return render(request, 'mastero_interiors/blog_list.html', context)

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    print("post are ",posts)
    paginator = Paginator(posts, 5)  # Show 5 blog posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Fetch popular blogs based on views
    popular_posts = BlogPost.objects.all().order_by('-views')[:5]

    context = {
        'posts':posts,
        'page_obj': page_obj,
        'popular_posts': popular_posts,
    }
    return render(request, 'mastero_interiors/blog_list.html', context)

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.views += 1
    post.save()

    # Get previous and next posts
    previous_post = BlogPost.objects.filter(id__lt=post.id).order_by('-id').first()
    next_post = BlogPost.objects.filter(id__gt=post.id).order_by('id').first()

    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    }
    return render(request, 'mastero_interiors/blog_detail.html', context)


@login_required
# @staff_member_required  # Ensure that only staff can access this page
def create_blog_post(request):
    # Check if the user is an admin (staff or superuser)
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to create blog posts.")

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to the admin page where the blog posts are listed
            return redirect('/admin/mastero_interiors/blogpost/')
        else:
            # Log or print form errors for debugging
            print(form.errors)
    else:
        form = BlogPostForm()

    return render(request, 'mastero_interiors/create_blog_post.html', {'form': form})

@login_required
def custom_edit_blog_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)

    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to edit blog posts.")

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('/admin/mastero_interiors/blogpost/')
        else:
            # Log or print form errors for debugging
            print(form.errors)
    else:
        form = BlogPostForm(instance=blog_post)

    return render(request, 'mastero_interiors/edit_blog_post.html', {'form': form, 'blog_post': blog_post})

