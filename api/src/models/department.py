from dataclasses import dataclass
from typing import NewType, Optional

DepartmentId = NewType('DepartmentId', str)

@dataclass
class Department:
    id: Optional[DepartmentId]
    name: str

    
