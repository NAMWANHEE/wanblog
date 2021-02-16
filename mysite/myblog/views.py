from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as au_lo,logout as au_logout
from django.urls import reverse
from .models import *
import getpass
def index(request):
    return render(request,'myblog/index.html')

def blog(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(username=username,password=password)

            return render(request, 'myblog/login.html')
        else:
            a = {'error':'비밀번호가 다릅니다'}
            return render(request, 'myblog/index.html',a)

def login(request):
    if request.method =="GET":
        return render(request,'myblog/login.html')
    elif request.method =="POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            au_lo(request,user)
            b = Post.objects.all()
            return redirect(reverse('main:post1'))
        else:
            error={'error':'회원정보가 일치하지 않습니다.'}
            return render(request,'myblog/login.html',error)



def post(request):
    if request.method == "POST":
        c = request.user
        post_name = request.POST['posting']
        text_name = request.POST['textname']
        a = Post(username=c,postname=post_name,contents=text_name)
        a.save()
    b = Post.objects.all()

    return render(request,'myblog/post.html',{'b':b})

def postD(request , pk):
    a = Post.objects.get(pk=pk)

    return render(request,'myblog/postD.html',{'a':a})
def create(request):
    return render(request,'myblog/create.html')

def logout(request):
    au_logout(request)
    return redirect('/')
# Create your views here.
