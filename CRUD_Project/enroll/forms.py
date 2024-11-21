from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control mt-2'}),'email':forms.EmailInput(attrs={'class':'form-control mt-2'}),'password':forms.PasswordInput(attrs={'class':'form-control mt-2'}),}