import attr

from typing import Optional

@attr.dataclass
class User:
    name: Optional[str] = None
    password: Optional[str] = None
    id: Optional[int] = None



