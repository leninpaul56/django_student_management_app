import email
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    usertype=models.CharField(max_length=50)


class addemployee1(models.Model):
    em_name=models.CharField(max_length=100)
    em_email=models.CharField(max_length=100)
    em_place=models.CharField(max_length=50)
    class Meta:
        db_table='employeeform'


class addstudent1(models.Model):
    st_name=models.CharField(max_length=100)
    st_regno=models.CharField(max_length=100)
    st_place=models.CharField(max_length=100)
    st_dept=models.CharField(max_length=100)
    st_mob=models.CharField(max_length=100)
    class Meta:
        db_table='studentform'