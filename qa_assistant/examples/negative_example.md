# /negative example

## Вход

`/negative API создания заказа: user_id, product_id, quantity от 1 до 99.`

## Идеальный ответ

| ID | Категория | Проверка | Тестовые данные | Ожидаемый результат | Приоритет |
|---|---|---|---|---|---|
| NEG-001 | Пустое поле | Отправить запрос без user_id | `{ "product_id": 10, "quantity": 1 }` | 400 Bad Request, ошибка обязательного поля | High |
| NEG-002 | Несуществующий ID | Передать несуществующий product_id | `product_id: 999999999` | 404 Not Found или бизнес-ошибка | High |
| NEG-003 | Вне диапазона | quantity = 0 | `quantity: 0` | 400 Bad Request | Medium |
| NEG-004 | Вне диапазона | quantity = 100 | `quantity: 100` | 400 Bad Request | Medium |
| NEG-005 | Неверный тип | quantity строкой | `quantity: "one"` | 400 Bad Request | Medium |
