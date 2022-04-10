from classic.app.errors import AppError


class NoBook(AppError):
    msg_template = "No book with ID '{number}'"
    code = 'no_user'


class BookTaken(AppError):
    msg_template = "Book is already taken by user with ID '{number}"
    code = 'book_taken'
