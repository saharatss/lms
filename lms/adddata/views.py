# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
#from .models import Weather

from django.http import JsonResponse
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
import sys
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

def home(request):
	return render(request,"home.html")

def show_add_page(request):
	return render(request,"add_page.html")

# MARK : main page

from .models import Class
from .models import Subject
from .models import Lesson
from .models import Chapter

web_name = "SCiUS TU-SKR Library"
path_link = [ 	{'name':"HOME",'link':"/class" }]
				#{'name':"LOGIN",'link':"/signin" }]

def add_page(request):
	if request.method == 'POST':
		test = request.POST.get('test', None)
		return HttpResponse(test, content_type='text/plain')
	return render(request,"page/add_page.html")

def class_page(request):
    class_data = Class.objects.all()
    class_title = []
    for i in class_data :
        class_title.append(i.title)
    return render(request,"page/class_page.html",{
        'class_title':class_title,
        'path_link':path_link,
        'web_name':web_name
        })


# MARK : Add contain

from django.shortcuts import redirect
from .forms import PostForm

from django.utils import timezone


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
            #return HttpResponse("Saved", content_type='text/plain')
            return redirect('post_new')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


# MARK : Login method

def signin(request):
	if request.method == 'POST' and 'username' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		print >>sys.stderr, "debug"
		if user is not None:
			if user.is_active:

				if 'remember' in request.POST:
					print>>sys.stderr, "%s type: %s"%(request.POST['remember'],type(request.POST['remember']))
					if request.POST['remember']=='1':
						request.session.set_expiry(604800) #remember keep session for a week
				else:
					request.session.set_expiry(14400) #not remember keep session for 4hrs
				print >>sys.stderr, "session expiry: %s"%request.session.get_expiry_age()

				login(request, user)
				if 'username' in request.session:
					print >>sys.stderr, "username_i: %s"%request.session['username']
				request.session['username'] = user.username
				print >>sys.stderr, "username_f: %s"%request.session['username']
				
				return redirect('post_new')
			else:
				msg="Disabled account"
		else:
			msg="Invalid username or password"
		return render(request,'login.html',{'msg': msg})   
	return render(request,'login.html',{'msg': ""})

def signout(request):
	print "signout"
	if 'username' in request.session:
		del request.session['username']
		print "del uname"
	logout(request)
	return redirect('signin')

@login_required(login_url='signin')
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    print >>sys.stderr, "request.user: %s"%request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('signin')

    return render(request, 'change_password.html', {
        'form': form,
    })


