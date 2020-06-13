from typing import Any

from pyramid.response import Response
from pyramid.request import Request
from sqlalchemy.sql import select
import cattr

from errors import EmployeeNotFound
from models import Employee, Envelope, Pagination, cursor_from_id, id_from_cursor
import db
from .util import json_endpoint

@json_endpoint
def get_employee(request: Request):
    employee_id = request.matchdict['id']

    employee = db.executeOne(Employee, select([db.employee]).where(db.employee.c.id == employee_id))
    if employee is None:
        raise EmployeeNotFound(employee_id)
    return employee

@json_endpoint
def get_employees(request: Request):
    # TODO add a wrapper params handler that allows you to specify the type
    # and handles validation errors automatically.
    page_size = request.params.get('page[size]')
    if page_size is None:
        page_size = 10
    else:
        page_size = int(page_size) # error thrown here

    page_after = request.params.get('page[after]')

    query = select([db.employee]).limit(page_size + 1).order_by(db.employee.c.id.asc())
    if page_after is not None:
        query = query.where(db.employee.c.id > id_from_cursor(page_after))

    employees = list(db.execute(Employee, query))
    next_id = None
    if len(employees) > page_size:
        next_id = employees[-1].id
        employees = employees[:-1]
    
    return Envelope(
        employees,
        Pagination(next = None if next_id is None else cursor_from_id(next_id))
    )

@json_endpoint
def post_employee(request: Request):
    # Validate that our input is correct
    payload = cattr.structure(request.json_body, Envelope[Employee])
    
    db.executeOne(Any, db.employee.insert().values(**cattr.unstructure(payload.data)))
    return Response(status_code=201) # Todo, handle 201 in json_endpoint probably use enum

@json_endpoint
def patch_employee(request: Request):
    employee_id = request.matchdict['id']
    
    # Validate that our input is correct
    payload = cattr.structure(request.json_body, Envelope[Employee])
    
    db.executeOne(Any, db.employee.insert().values(**cattr.unstructure(payload.data)).where(db.employee.c.id == employee_id))
    return Response(status_code=201) # Todo, handle 201 in json_endpoint probably use enum
