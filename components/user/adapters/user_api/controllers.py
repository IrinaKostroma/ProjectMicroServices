from classic.components import component

from user.application import services

from .join_points import join_point


@component
class Users:
    users: services.UserService

    @join_point
    def on_post_new_user(self, request, response):
        user = self.users.add_user(request.media)
        response.media = {
            'message': 'User added',
            'user_id': user.id,
            'name': user.name,
        }

    @join_point
    def on_get_all_users(self, request, response):
        users = self.users.get_all_users()
        response.media = [
            {
                'user_id': user.id,
                'name': user.name,
            } for user in users
        ]
