from classic.components import component

from book.application import services

from .join_points import join_point


@component
class Books:
    books: services.BookService

    @join_point
    def on_get_show_info(self, request, response):
        book = self.books.get_book(**request.media)
        response.media = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'user_id': book.user_id,
        }

    @join_point
    def on_get_all_books(self, request, response):
        books = self.books.get_all_books()
        response.media = [
            {
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'user_id': book.user_id
            } for book in books
        ]

    @join_point
    def on_post_new_book(self, request, response):
        book = self.books.add_book(request.media)
        response.media = {
            'message': 'Book added.',
            'title': book.title,
            'author': book.author,
        }

    @join_point
    def on_post_take_by_user(self, request, response):
        book = self.books.take_by_user(request.media)
        response.media = {
            'message': f'Book is taken by user with ID {book.user_id}.'
        }

    @join_point
    def on_post_return_book(self, request, response):
        book = self.books.return_book(request.media)
        response.media = {
            'message': f'Book ID {book.id} is now ready for booking.'
        }

    @join_point
    def on_post_remove_book(self, request, response):
        self.books.remove_book(**request.media)
        response.media = {
            'message': 'Book removed.'
        }
