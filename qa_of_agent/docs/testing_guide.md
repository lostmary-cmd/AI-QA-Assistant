# Как тестировать AI QA Assistant

## Шаг 1. Выбери команду

Например: `/testcases`.

## Шаг 2. Открой тест-кейсы

Файл:

```text
qa_of_agent/test_cases/TC001_testcases_cmd.md
```

## Шаг 3. Запусти агента

```bash
cd qa_assistant
python cli.py /testcases "Форма логина: email обязателен, пароль 8-32 символа"
```

## Шаг 4. Оцени ответ по метрикам

Открой:

```text
qa_of_agent/metrics/metrics_template.md
```

Поставь оценки:
- Полнота 0-10
- Форматирование 0-10
- Релевантность 0-10
- Отсутствие галлюцинаций 0/1
- Совпадение языка 0/1

## Шаг 5. Запиши результат

Добавь строку в:

```text
qa_of_agent/metrics/metrics_log.csv
```

## Шаг 6. Если ответ плохой — заведи баг

Используй шаблон:

```text
qa_of_agent/bug_reports/BUG_TEMPLATE.md
```

## Шаг 7. Исправь промпт

Например, если `/testcases` не даёт smoke-проверки, правь:

```text
qa_assistant/prompts/testcases_prompt.md
```

## Шаг 8. Запиши изменение в changelog

Файл:

```text
qa_of_agent/changelog/CHANGELOG.md
```
