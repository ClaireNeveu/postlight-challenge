from dataclasses import dataclass
from typing import NewType

DepartmentId = NewType('DepartmentId', str)

@dataclass
class Department:
    id: DepartmentId
    name: str

    
