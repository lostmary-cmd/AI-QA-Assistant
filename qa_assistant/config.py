"""Настройки AI QA Assistant.

Теперь основной режим — Ollama.
Ollama запускает модель локально на твоём компьютере.

По умолчанию:
- provider = ollama
- model = qwen2.5:3b
- url = http://localhost:11434/api/chat
"""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    provider: str = os.getenv("QA_ASSISTANT_PROVIDER", "ollama").lower()

    # Ollama settings
    ollama_model: str = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")
    ollama_url: str = os.getenv(
        "OLLAMA_URL",
        "http://localhost:11434/api/chat",
    )

    # OpenAI settings, если потом захочешь вернуть OpenAI
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    # Claude settings, если потом захочешь Claude
    anthropic_model: str = os.getenv(
        "ANTHROPIC_MODEL",
        "claude-3-5-sonnet-latest",
    )

    temperature: float = float(os.getenv("QA_ASSISTANT_TEMPERATURE", "0.2"))
    max_tokens: int = int(os.getenv("QA_ASSISTANT_MAX_TOKENS", "2500"))
    prompts_dir: str = os.getenv("QA_ASSISTANT_PROMPTS_DIR", "prompts")


settings = Settings()