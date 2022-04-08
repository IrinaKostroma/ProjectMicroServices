from classic.app.errors import AppError


class NoIssue(AppError):
    msg_template = "No issue with ID '{number}'"
    code = 'no_issue'
