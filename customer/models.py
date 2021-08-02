from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import date
from django.utils import timezone
# from django.db.models.fields.related import ForeignKey

# Create your models here.class
WORKTYPE_CHOICE = (
    ('Student','Student'),
    ('Driver','Driver'),
    ('Employee','Employee'),
    ('Shop owner','Shop owner'),
    ('Delivery boy','Delivery boy'),
    ('Other','Other')
)
ADDRESS_CHOICE = (
    ('Home with Family','Home with Family'),
    ('Rented with Family','Rented with Family'),
    ('Rented with Friends','Rented with Friends'),
    ('Hostel/PG','Hostel/PG')
)

class Personal_Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=30)
    Mother_Name =models.CharField(max_length=20,null=True)
    DOB = models.DateField(max_length=8,null=True)
    Age = models.IntegerField(null=True) 
    Pin_code = models.PositiveIntegerField()
    Work_Type = models.CharField(max_length=20, choices=WORKTYPE_CHOICE)
    Address_Type = models.CharField(max_length=50, choices=ADDRESS_CHOICE)
    Aadhar_Card_Number = models.PositiveBigIntegerField()
    Pan_Card_Number = models.CharField(max_length=16)

    def __str__(self):
        return self.Full_Name


class Document(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Front_Upload_Aadhar = models.ImageField(upload_to='customerdocuments',null=True)
    Back_Upload_Aadhar = models.ImageField(upload_to='customerdocuments',null=True)
    Upload_Pancard = models.ImageField(upload_to='customerdocuments',null=True, blank=True)
    Upload_Image = models.ImageField(upload_to='customerdocuments',null=True, blank=True)
    Upload_Income_Proof = models.ImageField(upload_to='customerdocuments',null=True, blank=True)
    Upload_Residence_Proof = models.ImageField(upload_to='customerdocuments',null=True, blank=True)

    def __str__(self):
        return self.user

TENURE_CHOICES = (
    ('3 month','3 month'),
    ('6 month','6 month'),
    ('9 month','9 month'),
    ('12 month', '12 month')
)
LOAN_CHOICES = (
    ('NEW','NEW'),
    ('APPROVED','APPROVED'),
    ('REJECTED','REJECTED')
)

class Apply_Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Company_Name = models.CharField(max_length=100)
    Salary = models.IntegerField()
    Amount_Need = models.IntegerField()
    Tenure = models.CharField(max_length=20, choices=TENURE_CHOICES)
    Rate = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    apply_date = models.DateTimeField(auto_now=timezone.now, blank=True, null=True)
    Loan_Status = models.CharField(max_length=30,choices=LOAN_CHOICES, null=True, default='pending')

    # created_on = models.DateTimeField(auto_now_add=True)


    @property
    def calculate_interest(self):
        amount = self.Amount_Need
        calc_interest = lambda value: value * self.Rate
        montly = []
        for i in range(12):
            interest = calc_interest(amount)
            amount += interest
            montly.append((i, amount, interest))
        return montly





    

   





