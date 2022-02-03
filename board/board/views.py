from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

def index(request):
    if 'username' in request.session:
        user = request.session['username']
        return render(request, 'board/index.html', user)
        return render(request, 'board/index.html')