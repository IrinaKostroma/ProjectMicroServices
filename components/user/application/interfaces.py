from abc import ABC, abstractmethod
from typing import Optional, List

from .dataclasses import User


class UsersRepo(ABC):

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]: ...

    @abstractmethod
    def get_all_users(self) -> List[User]: ...

    @abstractmethod
    def add(self, user: User): ...

    @abstractmethod
    def get_or_create(self, id_: Optional[int]) -> User: ...
