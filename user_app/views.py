from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from . forms import SignUpForm,LoginForm,PostForm
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib import messages


# Create your views here.
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
        else:
            form = SignUpForm()
        return render(request, 'user_app/signup.html',{'form':form})
    else:
        return HttpResponseRedirect('/addpost/')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/addpost/')
        else:
            form = LoginForm()
        return render(request, 'user_app/login.html', {'form':form})
    else:
        return HttpResponseRedirect ('/addpost/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                text_v = form.cleaned_data['text']
                pst = Post(user=request.user, text=text_v)
                pst.save()
                messages.success(request, 'Post Added Successfully!!')
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'user_app/addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')