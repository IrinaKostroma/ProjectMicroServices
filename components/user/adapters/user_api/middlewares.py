import falcon
import jwt
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend
import hashlib

SECRET = 'Big secret'

AUTH_BACKEND = JWTAuthBackend(
    lambda item: {'user_id': item.get('user').get('user_id')},
    SECRET,
    auth_header_prefix='Bearer'
)


class UserAuth(FalconAuthMiddleware):
    def process_resource(self, req, resp, resource, *args, **kwargs):
        auth_setting = self._get_auth_settings(req, resource)
        if (req.path in auth_setting['exempt_routes'] or
                req.method in auth_setting['exempt_methods']):
            return

        backend = auth_setting['backend']
        req.context['user'] = backend.authenticate(req, resp, resource, **kwargs)
        req.media.update(backend._decode_jwt_token(req).get('user'))

# --------------------------------
#
# SECRET = "DFSDDF2345msf23asdfs"
#
# USERS = {
#     "admin":
#         {
#             "login": "admin",
#             "password": hashlib.sha256("password".encode()).hexdigest()
#         }
# }

# class AddHeaderComponent:
#     def process_response(self, req, resp, resource, req_succeeded):
#         resp.set_header('X-Request-Name', '*')
#         resp.set_header('Content-Type', 'application/json')
#         resp.set_header('Access-Control-Max-Age', '86400')


# class UserAuth(FalconAuthMiddleware):
#     def process_resource(self, req, resp, resource, *args, **kwargs):
#         if req.path == '/login/':
#             data = req.get_media()
#             if data.get('login') and data.get("password"):
#                 user = USERS.get(data.get('login'))
#                 if user and user.get("password") == hashlib.sha256(data.get("password").encode()).hexdigest():
#                     return True # Логин и пароль корректный
#                 else:
#                     raise falcon.HTTPUnauthorized
#
#         elif req.method == 'POST' or req.method == 'GET':  # требуется авторизации
#             if req.get_header("Authorization", required=True):
#                 header = req.get_header("Authorization", required=True).split(' ')
#                 token = header[1]
#
#                 result = jwt.decode(token, SECRET, algorithms=["HS256"])
#                 user = USERS.get(result.get('login'))
#
#                 if not user and not user.get("password") == hashlib.sha256(result.get("password").encode()).hexdigest():
#                     raise falcon.HTTPUnauthorized
#
#             else:
#                 raise Exception('Error')

#------------------------------------


AUTH_MIDDLEWARE = UserAuth(AUTH_BACKEND, exempt_routes=['/api/users/register', '/api/users/login', '/api/chats'])
