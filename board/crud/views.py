from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    post_list = Post.objects.all()
    #output = "\n".join([p.post_title for p in post_list])
    output = [p.post_title for p in post_list]
    context = {'post_list' : post_list,}
    #return HttpResponse("Hello, world. You're at the crud index.")
    return render(request, 'crud/index.html', context)

def detail(request, post_id):
    return HttpResponse("You're looking at post %s." %post_id)

def write(request, post_id):
    return HttpResponse("You're writing a post %s." %post_id)