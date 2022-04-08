from typing import Optional

import attr

@attr.dataclass
class Book:
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    id: Optional[int] = None



