from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post

def index(request):
    post_list = Post.objects.all()
    context = {'post_list' : post_list,}
    #return HttpResponse("Hello, world. You're at the crud index.")
    return render(request, 'crud/index.html', context)

def write(request):
    if request.method == 'POST':
        post = Post()
        post.post_title = request.POST['title']
        post.post_content = request.POST['content']
        post.save()
        return redirect('crud:index')
    #return render(request, 'crud/write.html')
    else:
        post = Post.objects.all()
        #return render(request, 'crud/write.html', {'post':post})
        return render(request, 'crud/write.html',)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    #return HttpResponse("You're looking at post %s." %post_id)
    return render(request, 'crud/detail.html', {'post':post})
    #return HttpResponseRedirect(reverse('crud:index', args=(post.id,)))
    
    
def update(request, post_id):
    #posting = get_object_or_404(Post, pk=post_id)
    #return render(request, 'crud/update.html', {'post':post})
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id)
        post.post_content = request.POST['content']
        post.save()
        return redirect('crud:index')
    else:
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'crud/update.html', {'post':post})
