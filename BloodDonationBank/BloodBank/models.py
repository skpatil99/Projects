from django.db import models

# Create your models here.
class Donor(models.Model):
    Name = models.CharField(max_length = 64)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Blood_Grp = models.CharField(max_length=10)
    PhoneNo = models.IntegerField()

class Hospital(models.Model):
    Hospital_Code = models.IntegerField(db_index=True)
    Hos_Name = models.CharField(max_length=64)
    Blood_Grp = models.CharField(db_index=True,max_length=10)
    stock = models.IntegerField()

    Hos_Address = models.CharField(max_length=64)
    Hos_PhoneNo = models.IntegerField()
    Hos_Email = models.EmailField(max_length=64)

class UserDetail(models.Model):
    Hos_Code = models.IntegerField(db_index=True,primary_key=True)
    User_Name = models.CharField(max_length=100)
