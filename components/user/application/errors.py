from classic.app.errors import AppError


class NoUser(AppError):
    msg_template = "No user with ID '{number}'"
    code = 'no_user'


class NoMessage(AppError):
    msg_template = "No message'{number}'"
    code = 'no_message'


class NoChat(AppError):
    msg_template = "No chat '{number}'"
    code = 'no_chat'


class NoPermission(AppError):
    msg_template = "No permission"
    code = 'no_permisson'


class NoChatUsers(AppError):
    msg_template = "User isn`t in chat '{number}'"
    code = 'no_chatusers'


class RequestDenied(AppError):
    msg_template = "Request denied"
    code = 'request_denied'


class EmptyCart(AppError):
    msg_template = "Cart is empty"
    code = 'cart_is_empty'
