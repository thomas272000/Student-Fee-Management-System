from django.db import models
from datetime import date

# Create your models here.
class AdminModel(models.Model):
    name = models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    dob = models.DateField(default=date(1990, 1, 1))
    signup_date = models.DateField(auto_now_add=True)
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=20)
    roll_number = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.class_name})"


class FeeCategory(models.Model):
    name = models.CharField(max_length=100)
    fee_type = models.CharField(max_length=20)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.fee_type}"


class StudentFees(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_category = models.ForeignKey(FeeCategory, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='Due')
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    amount_paid = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student} - {self.fee_category} - {self.status}"
