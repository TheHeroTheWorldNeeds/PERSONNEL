from django.db import models
from django.db.models import Model


# Create your models here.

class Account(Model):
    username = models.CharField(verbose_name="User Name", max_length=50)
    password = models.CharField(verbose_name="User Password", max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('id',)


class Department(Model):
    id = models.CharField(verbose_name="Department ID", max_length=5, primary_key=True)
    name = models.CharField(verbose_name="Department Name", max_length=50)
    phone = models.CharField(verbose_name="Phone Number", max_length=15, null=True)

    def __str__(self):
        return self.name


class Position(Model):
    id = models.CharField(verbose_name="Position ID", max_length=5, primary_key=True)
    name = models.CharField(verbose_name="Position Name", max_length=50)

    def __str__(self):
        return self.name


class Salary(Model):
    salary_grade = models.IntegerField(verbose_name="Salary Grade", primary_key=True)
    basic_salary = models.IntegerField(verbose_name="Basic Salary")
    salary_coefficient = models.IntegerField(verbose_name="Salary Coefficient")
    allowance_coefficient = models.IntegerField(verbose_name="Allowance Coefficient")

    def __str__(self):
        return str(self.salary_grade)


class Staff(Model):
    name = models.CharField(verbose_name="Full Name", max_length=50)
    ethnic_group = models.CharField(verbose_name="Ethnic Group", max_length=20)
    gender = models.CharField(verbose_name="Gender", max_length=7)
    address = models.CharField(verbose_name="Address", max_length=200)
    dob = models.DateField(verbose_name="Date of Birth", )
    phone = models.CharField(verbose_name="Phone Number", max_length=15)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary_grade = models.ForeignKey(Salary, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
