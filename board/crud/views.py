from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# 함수형 view 대신 클래스형 view (=generic view)를 사용하면 코드가 더 간결해짐
# https://docs.djangoproject.com/ko/4.0/intro/tutorial04/ 제너릭뷰 변환 튜토리얼
# 하지만 학습과정에선 함수형 view로 학습해서 로직이해하는것을 추천

@login_required
# 로그인된 사용자만 해당 뷰를 볼 수 있도록 한다
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

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('crud:index')
    else:
        #return HttpResponse("You're looking at post %s." %post_id)
        return render(request, 'crud/detail.html', {'post':post})
        #return HttpResponseRedirect(reverse('crud:index', args=(post.id,)))