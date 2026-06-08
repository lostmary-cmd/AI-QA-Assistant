"""CLI запуск AI QA Assistant.

Пример:
python cli.py /testcases "Форма логина: email обязателен, пароль 8-32 символа"
"""

from __future__ import annotations

import sys

from agent import QAAssistantError, ask_agent


def main() -> int:
    if len(sys.argv) < 3:
        print(
            "Использование:\n"
            "python cli.py /testcases \"описание функции\"\n\n"
            "Команды:\n"
            "/testcases, /checklist, /weakspots, /negative, "
            "/bugreport, /http, /interview"
        )
        return 1

    command = sys.argv[1]
    payload = " ".join(sys.argv[2:])
    message = f"{command} {payload}"

    try:
        answer = ask_agent(message)
    except QAAssistantError as error:
        print(f"Ошибка: {error}")
        return 1
    except Exception as error:
        print(f"Неожиданная ошибка: {error}")
        return 1

    print(answer)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
