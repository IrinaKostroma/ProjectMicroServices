import attr
from datetime import datetime
from typing import Optional


@attr.dataclass
class Issue:
    action: str
    user_id: int
    book_id: int
    created: datetime
    id: Optional[int] = None
