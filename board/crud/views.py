from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post

def index(request):
    post_list = Post.objects.all()
    context = {'post_list' : post_list,}
    #return HttpResponse("Hello, world. You're at the crud index.")
    return render(request, 'crud/index.html', context)

def write(request):
    return render(request, 'crud/write.html')

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        selected_post = post.choice_set.get(pk=request.POST['title'])
    except (KeyError, Post.DoesNotExist):
        return render(request, 'crud/write.html', {'post':post, 'error_message':"You didn't write post.",})
    else:
        selected_post.save()
    #return HttpResponse("You're looking at post %s." %post_id)
    #return (request, 'crud/detail.html', {'post':post})
    return HttpResponseRedirect(reverse('crud:index', args=(post.id,)))

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'crud/update.html', {'post':post})
