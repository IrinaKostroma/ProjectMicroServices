from classic.app.errors import AppError


class NoIssue(AppError):
    msg_template = "No issue with ID '{number}'"
    code = 'no_issue'


class RequestDenied(AppError):
    msg_template = "Request denied"
    code = 'request_denied'
