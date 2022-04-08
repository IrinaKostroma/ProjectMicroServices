from classic.components import component

from book.application import services

from .join_points import join_point


@component
class Books:
    books: services.BookService

    @join_point
    def on_post_new_book(self, request, response):
        book = self.books.add_book(request.media)
        response.media = {
            'message': 'Book added',
            'title': book.title,
            'author': book.author,
        }

    @join_point
    def on_get_all_books(self, request, response):
        books = self.books.get_all_books()
        response.media = [
            {
                'book_id': book.id,
                'title': book.title,
                'author': book.author,
            } for book in books
        ]
