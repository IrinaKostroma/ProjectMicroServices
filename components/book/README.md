# Microservice Book

BookService - работа с книгами (CRUD)

URL для запросов:

POST 0.0.0.0:80/api/books/add_book       -  создание книги
GET 0.0.0.0:80/api/books/get_book?id=1   -  получение информации о книге
GET 0.0.0.0:80/api/books/get_all_books   -  получение информации о всех книгах
POST 0.0.0.0:80/api/books/take_by_user   - взять книгу
POST 0.0.0.0:80/api/books/return_book    - вернуть книгу
POST 0.0.0.0:80/api/books/remove_book    - удалить книгу
