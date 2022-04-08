from typing import Optional, List

from classic.components import component
from classic.sql_storage import BaseRepository
from sqlalchemy import select

from user.application import interfaces
from user.application.dataclasses import User


@component
class UsersRepo(BaseRepository, interfaces.UsersRepo):

    def get_by_id(self, id_: int) -> Optional[User]:
        query = select(User).where(User.id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def get_all_users(self) -> List[User]:
        query = select(User)  # .order_by(User.id)
        return self.session.execute(query).scalars().all()

    def add(self, user: User):
        self.session.add(user)
        self.session.flush()
        self.session.commit()

    def get_or_create(self, id_: Optional[int]) -> User:
        if id_ is None:
            user = User()
            self.add(user)
        else:
            user = self.get_by_id(id_)
            if user is None:
                user = User()
                self.add(user)
        return user
