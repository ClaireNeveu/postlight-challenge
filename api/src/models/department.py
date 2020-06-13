from dataclasses import dataclass
from typing import NewType, Optional

import cattr

DepartmentId = NewType('DepartmentId', str)

@dataclass
class Department:
    id: Optional[DepartmentId]
    name: str


# Serialization. cattr is basically Jackson for python.
# Instead of using the global cattr we'd be better off compiling
# an optimized converter that we attach to pyramid
# but I'm using the global here to save setup time.
cattr.register_structure_hook(Department, lambda d, typ: Department(**d))
cattr.register_unstructure_hook(Department, lambda e: asdict(e))

    
