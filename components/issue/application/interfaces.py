from abc import ABC, abstractmethod
from typing import List

from .dataclasses import Issue


class IssuesRepo(ABC):

    @abstractmethod
    def get_all(self) -> List[Issue]: ...

    @abstractmethod
    def add(self, issue: Issue): ...
