from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import CustomerDetails,Job

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username' ,label_suffix='',max_length=70, required=True, widget = forms.TextInput(attrs={'class':'form-control mb-2'}))
    password = forms.CharField(label='Password',label_suffix='', required=True, widget = forms.PasswordInput(attrs={'class':'form-control mt-2'}))


class AddUser(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password ',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','password1','password2']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}


class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ['studio_name','full_name', 'mobile','address','state','city','pincode']
        widgets = {
            'studio_name': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter Studio Name'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter Full Name'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter Mobile Number'}),
            'address': forms.Textarea(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter Address', 'rows': 3}),
            'state': forms.Select(attrs={'class': 'form-control mt-2'}),
            'city': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter City'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Enter Pincode'}),}



class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [ 'date', 'delivery_date', 'product_name', 'make', 'model','serial_number', 'customer_issues', 'collected_accessories','service_charge', 'parts_charge']

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'delivery_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'make': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_issues': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'collected_accessories': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'service_charge': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.00','value':'0.00'}),
            'parts_charge': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.00','value':'0.00'}),}

        labels = {'date': 'Date','delivery_date': 'Delivery Date','product_name': 'Product Name','make': 'Make','model': 'Model','serial_number': 'Serial Number','customer_issues': 'Customer Issues','collected_accessories': 'Collected Accessories','service_charge': 'Service Charge (₹)','parts_charge': 'Parts Charge (₹)',}