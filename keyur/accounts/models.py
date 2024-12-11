from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from decimal import Decimal
import datetime
# Create your models here.

STATE_CHOICE = (
 ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
 ('Andhra Pradesh','Andhra Pradesh'),
 ('Arunachal Pradesh','Arunachal Pradesh'),
 ('Assam','Assam'),
 ('Bihar','Bihar'),
 ('Chandigarh','Chandigarh'),
 ('Chhattisgarh','Chhattisgarh'),
 ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
 ('Daman and Diu','Daman and Diu'),
 ('Delhi','Delhi'),
 ('Goa','Goa'),
 ('Gujarat','Gujarat'),
 ('Haryana','Haryana'),
 ('Himachal Pradesh','Himachal Pradesh'),
 ('Jammu & Kashmir','Jammu & Kashmir'),
 ('Jharkhand','Jharkhand'),
 ('Karnataka','Karnataka'),
 ('Kerala','Kerala'),
 ('Lakshadweep','Lakshadweep'),
 ('Madhya Pradesh','Madhya Pradesh'),
 ('Maharashtra','Maharashtra'),
 ('Manipur','Manipur'),
 ('Meghalaya','Meghalaya'),
 ('Mizoram','Mizoram'),
 ('Nagaland','Nagaland'),
 ('Odisha','Odisha'),
 ('Puducherry','Puducherry'),
 ('Punjab','Punjab'),
 ('Rajasthan','Rajasthan'),
 ('Sikkim','Sikkim'),
 ('Tamil Nadu','Tamil Nadu'),
 ('Telangana','Telangana'),
 ('Tripura','Tripura'),
 ('Uttarakhand','Uttarakhand'),
 ('Uttar Pradesh','Uttar Pradesh'),
 ('West Bengal','West Bengal'),
)

class CustomerDetails(models.Model):
    studio_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=70)
    mobile = models.CharField(max_length=15,validators=[RegexValidator(regex=r'^\d{10}$', message='Enter a valid 10-digit mobile number')])
    address = models.TextField()
    state = models.CharField(max_length=50, choices=STATE_CHOICE)
    city = models.CharField(max_length=70)
    pincode = models.CharField(max_length=10)


class Job(models.Model):
    user = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False,default= datetime.date.today())
    delivery_date = models.DateField(default= datetime.date.today() + datetime.timedelta(days=2))
    product_name = models.CharField(max_length=70)
    make = models.CharField(max_length=70)
    model = models.CharField(max_length=70)
    serial_number = models.CharField(max_length=100)
    customer_issues = models.TextField()
    collected_accessories = models.TextField()
    service_charge = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    parts_charge = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])




