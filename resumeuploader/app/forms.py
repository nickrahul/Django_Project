from django import forms
from .models import Resume

GENDER_CHOICES = (
    ('Male','Male'),
    ('Female','Female')
)

JOB_CITY_CHOICE = [
    ('Delhi','Delhi'),
    ('Pune','Pune'),
    ('Ranchi','Ranchi'),
    ('Mumbai','Mumbai'),
    ('Dhanbad','Dhanbad'),
    ('Banglore','Banglore')
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    job_city = forms.MultipleChoiceField(label='Preferred Job Location',choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']
        labels = {'name':'Full Name','dob':'Date of Birth','pin':'Pin Code','mobile':'Mobile No','email':'Email ID','profile_image':'Profile Image','my_file':'Document'}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'dob':forms.DateInput(attrs={'class':'form-control','type':'date'}),'locality':forms.TextInput(attrs={'class':'form-control'}),'city':forms.TextInput(attrs={'class':'form-control'}),'pin':forms.NumberInput(attrs={'class':'form-control'}),'state':forms.Select(attrs={'class':'form-control'}),'mobile':forms.TextInput(attrs={'class':'form-control','type':'tel'}),'email':forms.EmailInput(attrs={'class':'form-control'}),'profile_image':forms.ClearableFileInput(attrs={'class': 'form-control mb-2'}),'my_file':forms.ClearableFileInput(attrs={'class':'form-control'})}