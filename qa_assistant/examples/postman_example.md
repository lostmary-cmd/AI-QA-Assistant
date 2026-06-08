# Postman Example

## Входные данные

```text
POST /login

Поля:
- email
- password
Пример ответа
Request

Method:

POST

URL:

{{base_url}}/login

Headers:

{
  "Content-Type": "application/json"
}

Body:

{
  "email": "user@test.com",
  "password": "Password123"
}
Positive Checks
Успешный логин
Возвращается access_token
Negative Checks
Пустой email
Пустой пароль
Неверный пароль
Postman Tests Script
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});