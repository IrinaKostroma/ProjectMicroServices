from classic.app.errors import AppError


class NoUser(AppError):
    msg_template = "No user with ID '{number}'"
    code = 'no_user'
