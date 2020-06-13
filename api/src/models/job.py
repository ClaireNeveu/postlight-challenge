from dataclasses import dataclass
from typing import NewType, Optional

import cattr

JobId = NewType('JobId', str)

@dataclass
class Job:
    id: Optional[JobId]
    name: str
    description: str


# Serialization. cattr is basically Jackson for python.
# Instead of using the global cattr we'd be better off compiling
# an optimized converter that we attach to pyramid
# but I'm using the global here to save setup time.
cattr.register_structure_hook(Job, lambda d, typ: Job(**d))
cattr.register_unstructure_hook(Job, lambda e: asdict(e))
