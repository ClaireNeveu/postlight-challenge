from dataclasses import dataclass
from typing import NewType

JobId = NewType('JobId', str)

@dataclass
class Job:
    id: JobId
    name: str
    description: str

    
