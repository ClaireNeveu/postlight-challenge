from pyramid.response import Response
from sqlalchemy.sql import select
import cattr

from errors import EmployeeNotFound
from models import Employee
import db
from .util import json_endpoint

@json_endpoint
def get_employee(request):
    employee_id = request.params.id
    
    employee = db.executeOne(Employee, select([db.employee]).where(db.employee.c.id == employee_id))
    if employee is None:
        raise EmployeeNotFound(employee_id)
    return employee
