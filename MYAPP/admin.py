from django.contrib import admin
from .models import Account, Department, Position, Salary, Staff

# Register your models here.
admin.site.register(Account)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Salary)
admin.site.register(Staff)
