from typing import Optional, List
from datetime import datetime

from classic.components import component
from classic.aspects import PointCut
from classic.app import DTO
from classic.messaging import Message, Publisher
from pydantic import validate_arguments

from .dataclasses import User
from .errors import NoUser
from .import interfaces


join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    id: Optional[int]
    name: str = None
    password: str = None


@component
class UserService:
    users_repo: interfaces.UsersRepo
    publisher: Publisher

    @join_point
    @validate_arguments
    def add_user(self, user_info: UserInfo) -> User:
        user = user_info.create_obj(User)
        self.users_repo.add(user)

        if self.publisher:
            self.publisher.plan(
                Message('log', {'action': 'add_user',
                                'user_id': user.id,
                                'book_id': None,
                                'created': datetime.now()
                                })
            )
        return user

    @join_point
    @validate_arguments
    def get_user(self, id: int) -> User:
        user = self.users_repo.get_by_id(id)
        if user is None:
            raise NoUser(number=id)
        return user

    @join_point
    @validate_arguments
    def get_all_users(self) -> List[User]:
        users = self.users_repo.get_all()
        return users

    @join_point
    @validate_arguments
    def remove_user(self, id: int):
        user = self.get_user(id)
        self.users_repo.remove(user)
