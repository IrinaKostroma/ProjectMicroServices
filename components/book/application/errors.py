from classic.app.errors import AppError


class NoBook(AppError):
    msg_template = "No book with ID '{number}'"
    code = 'no_user'


class RequestDenied(AppError):
    msg_template = "Request denied"
    code = 'request_denied'
