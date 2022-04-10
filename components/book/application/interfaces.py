from abc import ABC, abstractmethod
from typing import Optional, List

from .dataclasses import Book


class BooksRepo(ABC):

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[Book]: ...

    @abstractmethod
    def get_all(self) -> List[Book]: ...

    @abstractmethod
    def add(self, book: Book): ...

    @abstractmethod
    def get_or_create(self, id_: Optional[int]) -> Book: ...

    @abstractmethod
    def remove(self, book: Book) -> None: ...
