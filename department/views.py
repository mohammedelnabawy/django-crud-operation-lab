from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from department.models import Department

def departments_index(request):
    departments =Department.get_all_departments()
    return render(request, 'departments.html',
                  context={"departments":departments})


def show_dept(request, dept_id):
    department = Department.get_specific_department(dept_id)
    return render(request, 'show.html',
                  context={"department": department})


def delete_dept(request, dept_id):
    department = Department.get_specific_department(dept_id)
    department.delete()
    redirect_url = reverse('departments.index')
    return redirect(redirect_url)