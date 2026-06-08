# Настройка GitHub Projects как Jira

## Колонки доски

1. Backlog
2. In Progress
3. Review
4. Done

## Labels

- `bug` — плохой ответ агента
- `improvement` — улучшение промпта
- `task` — задача
- `epic` — большая задача
- `prompt` — связано с промптом
- `qa` — связано с тестированием
- `ai-response` — связано с качеством ответа

## Milestones

- `Prompt Quality v1`
- `QA Coverage v1`
- `Release v1`

## Workflow

### Backlog
Все новые issues попадают сюда.

### In Progress
Issue переносится сюда, когда исполнитель начал работу.

### Review
Issue переносится сюда, когда создан PR или промпт нужно проверить.

### Done
Issue переносится сюда, когда:
- PR merged;
- тесты пройдены;
- changelog обновлён.

## Автоматизации

В GitHub Projects можно настроить:

1. When issue is created → Backlog
2. When issue is assigned → In Progress
3. When pull request is linked → Review
4. When pull request is merged → Done
5. When issue is closed → Done

## Как использовать как Jira

- Epic = большая цель, например "Улучшить /testcases"
- Bug = плохой ответ агента
- Task = написать тесты или документацию
- Improvement = улучшить конкретный prompt
