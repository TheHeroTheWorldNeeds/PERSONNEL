from rest_framework import serializers
from MYAPP.models import Account, Department, Position, Salary, Staff


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password']


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'phone']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ['salary_grade', 'basic_salary', 'salary_coefficient', 'allowance_coefficient']


class StaffSerializer(serializers.ModelSerializer):
    position_name = serializers.ReadOnlyField(source="position_id.name")
    department_name = serializers.ReadOnlyField(source="department_id.name")
    basic_salary = serializers.ReadOnlyField(source="salary_grade.basic_salary")
    salary_coefficient = serializers.ReadOnlyField(source="salary_grade.salary_coefficient")
    allowance_coefficient = serializers.ReadOnlyField(source="salary_grade.allowance_coefficient")

    class Meta:
        model = Staff
        fields = ['id', 'name', 'ethnic_group', 'gender', 'address', 'dob', 'phone', 'position_id', 'position_name',
                  'department_id',
                  'department_name', 'salary_grade', 'basic_salary', 'salary_coefficient', 'allowance_coefficient']
