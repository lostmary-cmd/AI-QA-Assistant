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

## Roadmap

* [x] Test Cases Generator
* [x] Checklist Generator
* [x] Bug Report Generator
* [x] HTTP Helper
* [ ] Swagger Analyzer
* [ ] Postman Collection Generator
* [ ] SQL Test Generator
* [ ] Export to Excel

---

## Author

Slava Kazansky
QA Engineer / AI QA Enthusiast
