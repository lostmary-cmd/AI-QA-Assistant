# Swagger Example

## Входные данные

```text
POST /users

Создание пользователя.

Поля:
- name (string)
- email (string)
- age (integer)
Пример ответа
Positive Tests
Создание пользователя с валидными данными
Создание пользователя с минимально допустимым возрастом
Создание пользователя с максимально допустимым возрастом
Negative Tests
Отсутствует email
Некорректный email
Отрицательный возраст
SQL Injection в поле name
XSS в поле name
Status Codes
201 Created
400 Bad Request
409 Conflict
500 Internal Server Error