from abc import ABC, abstractmethod
from typing import List

from .dataclasses import Issue


class IssuesRepo(ABC):

    @abstractmethod
    def get_all_issues(self) -> List[Issue]: ...

    @abstractmethod
    def add(self, book: Issue): ...
