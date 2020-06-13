from dataclasses import dataclass, asdict
from typing import NewType, Optional

import cattr

from .job import JobId
from .department import DepartmentId

EmployeeId = NewType('EmployeeId', str)

@dataclass
class Employee:
    id: Optional[EmployeeId]
    name: str
    photo_id: str
    job: JobId
    department: DepartmentId
    location: str

# Serialization. cattr is basically Jackson for python.
# Instead of using the global cattr we'd be better off compiling
# an optimized converter that we attach to pyramid
# but I'm using the global here to save setup time.
cattr.register_structure_hook(Employee, lambda d, typ: Employee(**d))
cattr.register_unstructure_hook(Employee, lambda e: asdict(e))
