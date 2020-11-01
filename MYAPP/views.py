from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from MYAPP.models import Account, Department, Position, Salary, Staff
from MYAPP.serializers import AccountSerializer, DepartmentSerializer, PositionSerializer, SalarySerializer, \
    StaffSerializer
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST'])
def accounts_list(req):
    if req.method == 'GET':
        accounts = Account.objects.all()

        id = req.query_params.get('id', None)
        if id is not None:
            accounts = accounts.filter(id__exact=id)

        username = req.query_params.get('username', None)
        if username is not None:
            accounts = accounts.filter(username__exact=username)

        password = req.query_params.get('password', None)
        if password is not None:
            accounts = accounts.filter(password__exact=password)

        serializer = AccountSerializer(accounts, many=True)
        return JsonResponse(serializer.data, safe=False)
        # safe=False for objects serialization

    elif req.method == 'POST':
        accounts_data = JSONParser().parse(req)
        accounts_serializer = AccountSerializer(data=accounts_data)
        if accounts_serializer.is_valid():
            accounts_serializer.save()
            return JsonResponse(accounts_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(accounts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def accounts_detail(req, pk):
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return JsonResponse({'message': 'The account does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = AccountSerializer(account)
        return JsonResponse(serializer.data)

    elif req.method == 'PUT':
        account_data = JSONParser().parse(req)
        serializer = AccountSerializer(account, data=account_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method == 'DELETE':
        account.delete()
        return JsonResponse({'message': 'The account was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def departments_list(req):
    if req.method == 'GET':
        departments = Department.objects.all()

        id = req.query_params.get('id', None)
        if id is not None:
            departments = departments.filter(id__exact=id)

        serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(serializer.data, safe=False)
        # safe=False for objects serialization

    elif req.method == 'POST':
        departments_data = JSONParser().parse(req)
        dept_serializer = DepartmentSerializer(data=departments_data)
        if dept_serializer.is_valid():
            dept_serializer.save()
            return JsonResponse(dept_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(dept_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def departments_detail(req, pk):
    try:
        dept = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return JsonResponse({'message': 'The department does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = DepartmentSerializer(dept)
        return JsonResponse(serializer.data)

    elif req.method == 'PUT':
        dept_data = JSONParser().parse(req)
        serializer = DepartmentSerializer(dept, data=dept_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method == 'DELETE':
        dept.delete()
        return JsonResponse({'message': 'The department was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def positions_list(req):
    if req.method == 'GET':
        positions = Position.objects.all()

        id = req.query_params.get('id', None)
        if id is not None:
            positions = positions.filter(id__icontains=id)

        serializer = PositionSerializer(positions, many=True)
        return JsonResponse(serializer.data, safe=False)
        # safe=False for objects serialization

    elif req.method == 'POST':
        positions_data = JSONParser().parse(req)
        serializer = PositionSerializer(data=positions_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def positions_detail(req, pk):
    try:
        pos = Position.objects.get(pk=pk)
    except Position.DoesNotExist:
        return JsonResponse({'message': 'The position does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = PositionSerializer(pos)
        return JsonResponse(serializer.data)

    elif req.method == 'PUT':
        pos_data = JSONParser().parse(req)
        serializer = PositionSerializer(pos, data=pos_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method == 'DELETE':
        pos.delete()
        return JsonResponse({'message': 'The position was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def salaries_list(req):
    if req.method == 'GET':
        salaries = Salary.objects.all()

        salary_grade = req.query_params.get('salary_grade', None)
        if salary_grade is not None:
            salaries = salaries.filter(salary_grade__exact=salary_grade)

        serializer = SalarySerializer(salaries, many=True)
        return JsonResponse(serializer.data, safe=False)
        # safe=False for objects serialization

    elif req.method == 'POST':
        salaries_data = JSONParser().parse(req)
        serializer = SalarySerializer(data=salaries_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def salaries_detail(req, pk):
    try:
        salary = Salary.objects.get(pk=pk)
    except Salary.DoesNotExist:
        return JsonResponse({'message': 'The salary does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = SalarySerializer(salary)
        return JsonResponse(serializer.data)

    elif req.method == 'PUT':
        salary_data = JSONParser().parse(req)
        serializer = SalarySerializer(salary, data=salary_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method == 'DELETE':
        salary.delete()
        return JsonResponse({'message': 'The salary was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def staffs_list(req):
    if req.method == 'GET':
        staffs = Staff.objects.all()

        id = req.query_params.get('id', None)
        if id is not None:
            staffs = staffs.filter(id__exact=id)

        gender = req.query_params.get('gender', None)
        if gender is not None:
            staffs = staffs.filter(gender__exact=gender)

        position_id = req.query_params.get('position_id', None)
        if position_id is not None:
            staffs = staffs.filter(position_id__exact=position_id)

        department_id = req.query_params.get('department_id', None)
        if department_id is not None:
            staffs = staffs.filter(department_id__exact=department_id)

        salary_grade = req.query_params.get('salary_grade', None)
        if salary_grade is not None:
            staffs = staffs.filter(salary_grade__exact=salary_grade)

        serializer = StaffSerializer(staffs, many=True)
        return JsonResponse(serializer.data, safe=False)
        # safe=False for objects serialization

    elif req.method == 'POST':
        staffs_data = JSONParser().parse(req)
        serializer = StaffSerializer(data=staffs_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def staffs_detail(req, pk):
    try:
        staff = Staff.objects.get(pk=pk)
    except Staff.DoesNotExist:
        return JsonResponse({'message': 'The staff does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = StaffSerializer(staff)
        return JsonResponse(serializer.data)

    elif req.method == 'PUT':
        staff_data = JSONParser().parse(req)
        serializer = StaffSerializer(staff, data=staff_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method == 'DELETE':
        staff.delete()
        return JsonResponse({'message': 'The staff was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
