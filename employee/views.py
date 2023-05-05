from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.http import HttpResponse
from employee.models import Employee

employee_list=  ['Ahmed', 'Mohamed', 'Gehad']
def employee(request):
    return render(request, 'employee.html', context={"employee_list": employee_list})

def employee_index(request):
    employees = Employee.get_all_employee()
    return render(request, 'employees/index.html' ,context={"employees": employees})

def employee_show(request, id):
    employee = Employee.get_employee(id)
    return render(request, 'employees/show.html', context={"employee":employee})

def employee_delete(request, id):
    employee = Employee.get_employee(id)
    employee.delete()
    redirect_url = reverse('employees.index')
    return redirect(redirect_url)

from employee.forms import EmployeeForm
def create_employee(request):
    form = EmployeeForm()
    if request.method =='GET':
        return render(request, 'employees/create.html', context={"form":form})
    else:
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        # return HttpResponse("POST request received")
        redirect_url = reverse('employees.index')
        return redirect(redirect_url)


def edit_employee(request, id):
    employee = Employee.get_employee(id)
    form = EmployeeForm(instance=employee)
    if request.method =='GET':
        return render(request, 'employees/edit.html', context={"form":form})
    else:
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
        # return HttpResponse("POST request received")
        redirect_url = reverse('employees.index')
        return redirect(redirect_url)