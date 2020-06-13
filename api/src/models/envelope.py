from dataclasses import dataclass, asdict
from typing import TypeVar, Generic

import cattr

T = TypeVar('T')
@dataclass
class Envelope(Generic[T]):
    data: T


# Serialization. cattr is basically Jackson for python.
# Instead of using the global cattr we'd be better off compiling
# an optimized converter that we attach to pyramid
# but I'm using the global here to save setup time.
cattr.register_structure_hook(Envelope, lambda d, typ: Envelope(**d))
cattr.register_unstructure_hook(Envelope, lambda e: asdict(e))
