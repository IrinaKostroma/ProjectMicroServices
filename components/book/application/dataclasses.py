from typing import Optional

import attr

@attr.dataclass
class Book:
    id: Optional[int] = None
    title: Optional[str] = None
    author: Optional[str] = None
    user_id: Optional[int] = None



