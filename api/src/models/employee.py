from dataclasses import dataclass
from typing import NewType

from .job import JobId
from .department import DepartmentId

EmployeeId = NewType('EmployeeId', str)

@dataclass
class Employee:
    id: EmployeeId
    name: str
    photo_id: str
    job: JobId
    department: DepartmentId
    location: str

    
