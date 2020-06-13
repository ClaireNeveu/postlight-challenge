from typing import Any

from pyramid.response import Response
from sqlalchemy.sql import select
import cattr

from errors import EmployeeNotFound
from models import Employee, Envelope
import db
from .util import json_endpoint

@json_endpoint
def get_employee(request):
    employee_id = request.params['id']
    
    employee = db.executeOne(Employee, select([db.employee]).where(db.employee.c.id == employee_id))
    if employee is None:
        raise EmployeeNotFound(employee_id)
    return employee

@json_endpoint
def get_employees(request):    
    employees = db.execute(Employee, select([db.employee]).where(db.employee.c.id == employee_id))
    return employees

@json_endpoint
def post_employee(request):
    # Validate that our input is correct
    payload = cattr.structure(request.json_body, Envelope[Employee])
    
    db.executeOne(Any, db.employee.insert().values(**cattr.unstructure(payload.data)))
    return Response(status_code=201) # Todo, handle 201 in json_endpoint probably use enum

@json_endpoint
def patch_employee(request):
    employee_id = request.params['id']
    
    # Validate that our input is correct
    payload = cattr.structure(request.json_body, Envelope[Employee])
    
    db.executeOne(Any, db.employee.insert().values(**cattr.unstructure(payload.data)).where(db.employee.c.id == employee_id))
    return Response(status_code=201) # Todo, handle 201 in json_endpoint probably use enum
