# AI QA Assistant Project

Проект состоит из двух частей:

1. `qa_assistant` — сам AI QA Assistant.
2. `qa_of_agent` — QA-система для тестирования ответов агента.

## Полный цикл

### 1. Ввод

```bash
python cli.py /testcases "Форма логина: email обязателен, пароль 8-32 символа"
```

### 2. Ответ агента

Агент должен вернуть таблицу:

```text
ID | Название | Предусловие | Шаги | Ожидаемый результат | Приоритет
```

### 3. Тест-кейс

Берём тест из:

```text
qa_of_agent/test_cases/TC001_testcases_cmd.md
```

### 4. Баг-репорт

Если агент не добавил smoke-проверки, создаём баг по шаблону:

```text
qa_of_agent/bug_reports/BUG_TEMPLATE.md
```

### 5. Правка промпта

Правим:

```text
qa_assistant/prompts/testcases_prompt.md
```

Например, добавляем правило:

```text
Обязательно добавь минимум 1 smoke-проверку.
```

### 6. Changelog

Записываем изменение:

```text
qa_of_agent/changelog/CHANGELOG.md
```

## Запуск

Смотри инструкцию:

```text
qa_assistant/README.md
```
