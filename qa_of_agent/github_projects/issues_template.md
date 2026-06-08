# GitHub Issues templates

## Bug — плохой ответ агента

### Title
`[Bug] /command: краткое описание проблемы`

### Labels
`bug`, `ai-response`, `prompt`

### Milestone
`Prompt Quality v1`

### Assignee
QA owner

### Body
```markdown
## Команда
/command

## Входные данные

## Фактический ответ

## Ожидаемый ответ

## Почему это баг
- [ ] Нарушен формат
- [ ] Неполный ответ
- [ ] Нерелевантный ответ
- [ ] Галлюцинация
- [ ] Не тот язык

## Severity
Critical / Major / Minor

## Предложение по исправлению
```

---

## Improvement — улучшение промпта

### Title
`[Improvement] /command: что улучшить`

### Labels
`improvement`, `prompt`

### Milestone
`Prompt Quality v1`

### Assignee
Prompt engineer

### Body
```markdown
## Что хотим улучшить

## Почему это нужно

## Какой prompt-файл меняем

## Критерии готовности
- [ ] Улучшение добавлено
- [ ] Тесты пройдены
- [ ] Метрики улучшились
```

---

## Task — написать тест-кейс

### Title
`[Task] Добавить тест-кейс для /command`

### Labels
`task`, `qa`

### Milestone
`QA Coverage v1`

### Assignee
QA engineer

### Body
```markdown
## Команда

## Какой сценарий покрыть
- [ ] positive
- [ ] negative
- [ ] boundary
- [ ] smoke

## Где добавить файл/строку

## Definition of Done
- [ ] Тест-кейс добавлен
- [ ] Есть ожидаемый результат
- [ ] Есть критерии качества
```

---

## Epic — улучшение конкретной команды

### Title
`[Epic] Улучшить команду /command`

### Labels
`epic`, `prompt-quality`

### Milestone
`Prompt Quality v1`

### Assignee
QA architect

### Body
```markdown
## Цель

## Какие проблемы решаем

## Связанные Issues

## Метрики успеха
- Средний score >= 45/50
- Нет Critical bugs
- Формат соблюдается в 95% запусков
```
