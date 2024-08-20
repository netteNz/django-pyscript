from django.shortcuts import render
from django.templatetags.static import static
from blog.models import Post, Comment, Project  # Include the Project model
from django.core.paginator import Paginator
from django.http import JsonResponse

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    static_url = static('query.json')
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }
    return render(request, "blog/detail.html", context)

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    paginator = Paginator(projects, 6)  # Display 6 projects per page

    # Use request.headers to check if the request is an AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        page = request.GET.get('page')
        projects = paginator.get_page(page)
        return JsonResponse({
            'projects': list(projects.object_list.values('title', 'description', 'image', 'url'))
        })

    return render(request, 'blog/project_list.html', {'projects': paginator.get_page(1)})