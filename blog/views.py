from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserLoginFormLegit
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=user_password, email=email)
            #login(request, user)
            return redirect('post_list')
    else:
        form = UserLoginForm()
    return render(request, 'blog/register.html', {'form': form})

def logout_page(request):
    logout(request)
    return redirect('post_list')