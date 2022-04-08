import attr

from typing import Optional

@attr.dataclass
class User:
    name: str
    password: str
    id: Optional[int] = None



