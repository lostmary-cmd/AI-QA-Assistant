# AI QA Assistant

AI QA Assistant — это консольный ИИ-агент для QA-инженера.

Он умеет выполнять команды:

- `/testcases` — генерирует тест-кейсы
- `/checklist` — генерирует чек-лист
- `/weakspots` — анализирует требования
- `/negative` — генерирует негативные проверки
- `/bugreport` — оформляет баг-репорт
- `/http` — объясняет HTTP/API ошибки
- `/interview` — готовит вопросы для Junior QA interview

## Запуск за 5 шагов

### 1. Перейди в папку проекта

```bash
cd qa_assistant
```

### 2. Создай виртуальное окружение

```bash
python -m venv .venv
```

### 3. Активируй окружение

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Установи зависимости

```bash
pip install -r requirements.txt
```

### 5. Укажи API-ключ и запусти команду

OpenAI:

```bash
set OPENAI_API_KEY=your_api_key_here
python cli.py /testcases "Форма логина: email обязателен, пароль 8-32 символа"
```

macOS/Linux:

```bash
export OPENAI_API_KEY=your_api_key_here
python cli.py /testcases "Форма логина: email обязателен, пароль 8-32 символа"
```

## Переключение на Claude

```bash
set QA_ASSISTANT_PROVIDER=anthropic
set ANTHROPIC_API_KEY=your_api_key_here
python cli.py /checklist "Форма регистрации"
```

## Как это работает

1. `cli.py` принимает команду из терминала.
2. `agent.py` определяет команду.
3. Агент берёт общий системный промпт из `prompts/system_prompt.md`.
4. Потом добавляет промпт конкретной команды.
5. Отправляет всё в OpenAI или Claude API.
6. Возвращает готовый ответ в терминал.
