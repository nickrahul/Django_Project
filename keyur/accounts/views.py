from .forms import LoginForm,AddUser,CustomerDetailsForm,JobForm
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomerDetails


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            form.add_error(None, 'Invalid username or password!')

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def home(request):
    return render(request, 'accounts/home.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')


@login_required
def all_jobs(request):
    return render(request, 'accounts/all_jobs.html')


@login_required
def add_userr(request):
    if request.method == "POST":
        form = AddUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User added successfully!") 
            return redirect('add_user') 
        else:
            messages.error(request, "Please correct the errors below.")     
    else:
        form = AddUser()  # Empty form for GET request

    return render(request, 'accounts/add_user.html', {'form': form})


@login_required
def createjob(request):
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST)
        form2 = JobForm(request.POST)
        
        if form.is_valid() and form2.is_valid():
            customer = form.save()
            job = form2.save(commit=False)
            job.user = customer
            job.save()
            
            messages.success(request, "Job created successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomerDetailsForm()
        form2 = JobForm()

    return render(request, 'accounts/createjob.html', {'form': form, 'form2': form2})


@login_required
def customers(request):
    data = CustomerDetails.objects.all()
    return render(request, 'accounts/customers.html',{'data':data})