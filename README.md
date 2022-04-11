# Проект «Микросервисное взаимодействие»


Проект реализация взаимодействия 3 микросервисов User, Issue, Book.
nginx проксирует запросы ко всем сервисам и является точкой входа в систему.
Событийно ориентированная архитектура - микросервисы User и Book с помощью брокера сообщений RabbitMQ отправляют логи микросервису Issue. 
Хранение данных в базе данных PostgreSQL.
Для развертывания приложения используется Docker.  

UserService - URL для запросов:

POST 0.0.0.0:80/api/users/add_user   - добавить пользователя
GET 0.0.0.0:80/api/users/get_user    - получить информацию о пользователе
GET 0.0.0.0:80/api/users/get_all_users - получить информацию о всех пользователях
GET 0.0.0.0:80/api/users/remove_user   - удалить пользователя

BookService - URL для запросов:

POST 0.0.0.0:80/api/books/add_book       -  создание книги
GET 0.0.0.0:80/api/books/get_book?id=1   -  получение информации о книге
GET 0.0.0.0:80/api/books/get_all_books   -  получение информации о всех книгах
POST 0.0.0.0:80/api/books/take_by_user   - взять книгу
POST 0.0.0.0:80/api/books/return_book    - вернуть книгу
POST 0.0.0.0:80/api/books/remove_book    - удалить книгу

IssueService - URL для запросов:

GET 0.0.0.0:80/api/issues/get_all_issues - получить информацию обо всех событиях
