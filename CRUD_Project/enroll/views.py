from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User
# Create your views here.


def home(request):
    if request.method=='POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            reg = User(name=name, email=email, password=password)
            reg.save()
            form = StudentRegistration()
            return redirect('/')
    else:
        form = StudentRegistration()
    data = User.objects.all()
    return render(request, 'enroll/addandshow.html', {"form":form,"data":data})



def update_data(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        form = StudentRegistration(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        pi = User.objects.get(pk=id)
        form = StudentRegistration(instance=pi) 
    return render(request, 'enroll/update.html',{'form':form}) 




def delete_data(request, id):
    if request.method=="POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('/')