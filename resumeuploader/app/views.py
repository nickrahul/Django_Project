from django.shortcuts import render,redirect
from .forms import ResumeForm
from .models import Resume
from django.views import View
from django.contrib import messages
# Create your views here.



class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        data = Resume.objects.all()
        return render(request, 'app/home.html', {'form':form,'data':data})
    
    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form Submitted Successfully!')
            form = ResumeForm()
            return redirect('home')
        else:
            messages.error(request, 'There were errors in the form. Please correct them.')
        return render(request, 'app/home.html', {'form':form})
    
class Candidate(View):
    def get(self,request,id):
        data = Resume.objects.get(pk=id)
        return render(request, 'app/candidate.html',{'data':data})