from abc import ABC, abstractmethod
from typing import Optional

from .dataclasses import Issue


class IssuesRepo(ABC):

    @abstractmethod
    def get_all_issues(self) -> Optional[Issue]: ...

    @abstractmethod
    def add(self, book: Issue): ...
