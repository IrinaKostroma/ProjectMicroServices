import attr
from datetime import datetime
from typing import Optional


@attr.dataclass
class Issue:
    action: str
    created: datetime
    user_id: Optional[int] = None
    book_id: Optional[int] = None
    id: Optional[int] = None
