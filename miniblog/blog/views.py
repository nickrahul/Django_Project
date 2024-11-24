from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,LoginForm, PostForm, UserProfileUpdateForm
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

# Create your views here.


# Home
def home(request):
    data = Post.objects.all()
    return render(request, 'blog/home.html', {'data':data}) 

# About
def about(request):
    return render(request, 'blog/about.html')

# Contact
def contact(request):
    return render(request, 'blog/contact.html')


# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user.get_full_name()
        gps = request.user.groups.all()
        return render(request, 'blog/dashboard.html', {'post':posts,"user":user,"gp":gps})
    else:
        return redirect('login')

# Logout
def user_logout(request):
    logout(request)
    messages.info(request, "Logout successful!")
    return redirect('/')


# SignUp
def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            messages.success(request, "Registration successful! Please Proceed To Login.")
            return redirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html',{"form":form})


# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login successful!")
                    return redirect('dashboard')
                else:
                    form.add_error(None, "Invalid username or password.")
        else:
            form = LoginForm()
        return render(request, 'blog/login.html',{"form":form})
    else:
        return redirect('dashboard')
    

# Add New Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = PostForm(request.POST)
            if form.is_valid():
                ti = form.cleaned_data['title']
                desc = form.cleaned_data['description']
                data = Post(title=ti, description=desc)
                data.save()
                messages.success(request, "Post Added Succesfully")
                return redirect('dashboard')
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html',{'form':form} )
    else:
        return redirect('login')
    
# Update Post
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post Updated SuccessFully')
                return redirect ('dashboard')
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form':form})
    else:
        return redirect('login')


# Delete Post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method=='POST': 
            pi = Post.objects.get(pk=id)
            pi.delete()
        return redirect('dashboard')
    else:
        return redirect('login')
    

# Profile Updated Form

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile_update')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserProfileUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})