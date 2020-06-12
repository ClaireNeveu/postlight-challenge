from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')
@dataclass
class Envelope(Generic[T]):
    data: T
