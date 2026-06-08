"""AI QA Assistant — версия только под Ollama."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from pathlib import Path
from typing import Dict, Tuple


COMMAND_TO_PROMPT: Dict[str, str] = {
    "/testcases": "testcases_prompt.md",
    "/checklist": "checklist_prompt.md",
    "/weakspots": "weakspots_prompt.md",
    "/negative": "negative_prompt.md",
    "/bugreport": "bugreport_prompt.md",
    "/http": "http_prompt.md",
    "/interview": "interview_prompt.md",
}

OLLAMA_MODEL = "qwen2.5:3b"
OLLAMA_URL = "http://localhost:11434/api/chat"
TEMPERATURE = 0.2
MAX_TOKENS = 2500
PROMPTS_DIR = "prompts"


class QAAssistantError(Exception):
    """Ошибка AI QA Assistant."""


def project_dir() -> Path:
    return Path(__file__).resolve().parent


def read_prompt(filename: str) -> str:
    path = project_dir() / PROMPTS_DIR / filename

    if not path.exists():
        raise QAAssistantError(f"Не найден файл промпта: {path}")

    return path.read_text(encoding="utf-8")


def parse_user_message(message: str) -> Tuple[str, str]:
    clean_message = message.strip()

    if not clean_message:
        raise QAAssistantError("Пустой ввод. Укажи команду и описание.")

    parts = clean_message.split(maxsplit=1)
    command = parts[0].lower()
    payload = parts[1].strip() if len(parts) > 1 else ""

    if command not in COMMAND_TO_PROMPT:
        available = ", ".join(COMMAND_TO_PROMPT)
        raise QAAssistantError(
            f"Неизвестная команда: {command}\n"
            f"Доступные команды: {available}"
        )

    return command, payload


def build_messages(command: str, payload: str) -> list[dict[str, str]]:
    system_prompt = read_prompt("system_prompt.md")
    command_prompt = read_prompt(COMMAND_TO_PROMPT[command])

    user_content = (
        f"Команда: {command}\n"
        f"Входные данные пользователя:\n"
        f"{payload}"
    )

    return [
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": command_prompt},
        {"role": "user", "content": user_content},
    ]


def ask_ollama(messages: list[dict[str, str]]) -> str:
    request_body = {
        "model": OLLAMA_MODEL,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": TEMPERATURE,
            "num_predict": MAX_TOKENS,
        },
    }

    request_data = json.dumps(request_body, ensure_ascii=False).encode("utf-8")

    request = urllib.request.Request(
        OLLAMA_URL,
        data=request_data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            response_text = response.read().decode("utf-8")
    except urllib.error.URLError as error:
        raise QAAssistantError(
            "Не удалось подключиться к Ollama.\n\n"
            "Проверь:\n"
            "1. Ollama установлен.\n"
            "2. Ollama запущен.\n"
            f"3. Модель скачана: ollama pull {OLLAMA_MODEL}\n\n"
            f"Техническая ошибка: {error}"
        ) from error

    response_json = json.loads(response_text)

    if "message" not in response_json or "content" not in response_json["message"]:
        raise QAAssistantError(f"Неожиданный ответ Ollama:\n{response_json}")

    return response_json["message"]["content"]


def ask_agent(user_message: str) -> str:
    command, payload = parse_user_message(user_message)
    messages = build_messages(command, payload)
    return ask_ollama(messages)