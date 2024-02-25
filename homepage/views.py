from django.shortcuts import render, get_object_or_404, loader
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(request, 
                'homepage/post/list.html', 
                {'posts':posts}
    )

from django.http import Http404

def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    return render(request,
                'homepage/post/detail.html',
                {'post': post})

def post_detail(request, id):
    post = get_object_or_404(Post,
                            id=id,
                            status=Post.Status.PUBLISHED)
    return render(request,
                'homepage/post/detail.html',
                {'post': post})

def home(request):
    template = loader.get_template('homepage/nav/index.html')
    return HttpResponse(template.render())

def leaderboard(request):
    template = loader.get_template('homepage/leaderboard/leaderboard.html')
    return HttpResponse(template.render())
    
def apcsa(request):
    template = loader.get_template('homepage/courses/apcsa.html')
    return HttpResponse(template.render())

def bio(request):
    template = loader.get_template('homepage/courses/apbio.html')
    return HttpResponse(template.render())