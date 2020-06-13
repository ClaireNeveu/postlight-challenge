from dataclasses import dataclass, asdict
from typing import TypeVar, Generic, Optional

import cattr

from .cursor import Cursor

@dataclass
class Pagination:
    first: Optional[Cursor] = None
    last: Optional[Cursor] = None
    prev: Optional[Cursor] = None
    next: Optional[Cursor] = None

cattr.register_structure_hook(Pagination, lambda d, typ: Pagination(**d))
cattr.register_unstructure_hook(Pagination, lambda e: asdict(e))

# TODO handle undefined vs null in serialization here
T = TypeVar('T')
@dataclass
class Envelope(Generic[T]):
    data: T
    links: Optional[Pagination] = None


# Serialization. cattr is basically Jackson for python.
# Instead of using the global cattr we'd be better off compiling
# an optimized converter that we attach to pyramid
# but I'm using the global here to save setup time.
cattr.register_structure_hook(Envelope, lambda d, typ: Envelope(**d))
cattr.register_unstructure_hook(Envelope, lambda e: asdict(e))
