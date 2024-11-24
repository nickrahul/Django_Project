from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name', 'last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={"class":"form-control"}),'first_name':forms.TextInput(attrs={"class":"form-control"}),'last_name':forms.TextInput(attrs={"class":"form-control"}),'email':forms.EmailInput(attrs={"class":"form-control",'required':''}),}


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description']
        labels = {'title':'Title','description':'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}), 'description':forms.Textarea(attrs={'class':'form-control'})}


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),'first_name': forms.TextInput(attrs={'class': 'form-control'}),'last_name': forms.TextInput(attrs={'class': 'form-control'}),'email': forms.EmailInput(attrs={'class': 'form-control'}),}