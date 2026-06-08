# AI QA Assistant

AI QA Assistant — локальный помощник для QA-инженера на Python + Ollama.

## Возможности

### /testcases

Генерация тест-кейсов:

* Positive
* Negative
* Boundary
* Smoke

### /checklist

Генерация чек-листов:

* UI
* Functional
* Edge Cases

### /weakspots

Анализ требований:

* неоднозначности
* противоречия
* отсутствующие проверки
* вопросы к разработчику

### /negative

Генерация негативных сценариев:

* SQL Injection
* XSS
* Неверные типы данных
* Отсутствующие поля
* Несуществующие ID
* Конкурентные запросы

### /bugreport

Автоматическая генерация баг-репортов.

### /http

Справочник по HTTP и API ошибкам.

### /interview

Подготовка к собеседованию Junior QA.

### /swagger

Генерирует API тесты по описанию Swagger/OpenAPI endpoint.

Возможности:

* Позитивные API тесты
* Негативные API тесты
* Граничные проверки
* Проверки HTTP статус-кодов
* Проверки структуры ответа
* Проверки обязательных полей
* Проверки авторизации и аутентификации
* Анализ рисков и рекомендации QA

Пример:

```bash
python cli.py /swagger "POST /users"
```

### /postman

Генерирует готовые сценарии тестирования для Postman.

Возможности:

* Формирование Request Method
* Формирование URL endpoint
* Формирование Headers
* Примеры Authorization
* Примеры Request Body
* Позитивные проверки
* Негативные проверки
* Граничные проверки
* Проверки HTTP статус-кодов
* Генерация Postman Tests Script

Пример:

```bash
python cli.py /postman "POST /login email password"
```


---

## Технологии

* Python
* Ollama
* Qwen
* Git
* GitHub

---

## Установка

```bash
pip install -r requirements.txt
```

Установить Ollama:

```bash
ollama pull qwen2.5:3b
```

---

## Запуск

```bash
python cli.py /http "404"
```

Пример:

```bash
python cli.py /testcases "Форма логина"
```

---

## Архитектура

```text
CLI
↓
Agent
↓
Prompt Engine
↓
Ollama
↓
LLM Response
```

---

## План развития

* [x] Генератор тест-кейсов
* [x] Генератор чек-листов
* [x] Анализ требований
* [x] Генератор негативных сценариев
* [x] Генератор баг-репортов
* [x] Помощник по HTTP/API
* [x] Тренажёр QA-собеседований
* [x] Генератор Swagger API тестов
* [x] Генератор Postman сценариев
* [ ] Web-интерфейс на Streamlit
* [ ] Экспорт в Excel
* [ ] Экспорт в Qase/TestRail
* [ ] Генератор SQL-запросов

---

## Автор

Slava Kazansky
QA Engineer / AI QA Enthusiast
