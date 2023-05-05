from django.urls import path , include

    # from . import views
import employee.views
from employee.views import employee , employee_index, employee_show, employee_delete, create_employee, edit_employee


urlpatterns = [
    path("", employee, name="employee"),
    path("operation/", employee_index, name="employees.index"),
    path("operation/<int:id>", employee_show, name="employee.show"),
    path("operation/<int:id>/delete", employee_delete, name="employee.delete"),
    path("create/", create_employee, name="create.employee"),
    path("operation/<int:id>/edit", edit_employee, name="edit.employee")
]