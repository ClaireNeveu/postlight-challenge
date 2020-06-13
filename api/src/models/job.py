from dataclasses import dataclass
from typing import NewType, Optional

JobId = NewType('JobId', str)

@dataclass
class Job:
    id: Optional[JobId]
    name: str
    description: str

    
