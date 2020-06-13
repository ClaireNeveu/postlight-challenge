from dataclasses import dataclass, asdict
from base64 import urlsafe_b64encode, urlsafe_b64decode

from typing import NewType

# Cursor for use in pagination
Cursor = NewType('Cursor', str)

def cursor_from_id(ident: int) -> Cursor:
    """Converts an identifer to a database object (used to limit db queries)
    into an opaque cursor. This hides the implementation of pagination
    from the frontend.
    """
    return urlsafe_b64encode(str(ident).encode('utf-8')).decode('utf-8').strip('=')
    

def id_from_cursor(cursor: Cursor) -> int:
    """Converts a cursor to an identifier for pagination
    """
    padding_needed = len(cursor) % 4
    if padding_needed > 0:
        padding_needed = 4 - padding_needed
    cursor = cursor + ''.join(('=' for i in range(padding_needed)))
    return int(urlsafe_b64decode(cursor.encode('utf-8')).decode('utf-8'))
