from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def index(request):
    post_list = Post.objects.all()
    context = {'post_list' : post_list,}
    #return HttpResponse("Hello, world. You're at the crud index.")
    return render(request, 'crud/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    #return HttpResponse("You're looking at post %s." %post_id)
    return render(request, 'crud/detail.html', {'post':post})

def write(request, post_id):
    return HttpResponse("You're writing a post %s." %post_id)